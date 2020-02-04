#!/usr/bin/env bash

BASENAME="${0##*/}"
export HOME=/home/nobody

# Standard function to print an error and exit with a failing return code
error_exit () {
  echo "${BASENAME} - ${1}" >&2
  exit 1
}

# Check what environment variables are set
if [ -z "${AWS_ACCESS_KEY_ID}" ]; then
  echo "AWS_ACCESS_KEY_ID not set"
  exit 1
fi

if [ -z "${AWS_SECRET_ACCESS_KEY}" ]; then
  echo "AWS_SECRET_ACCESS_KEY not set"
  exit 1
fi

if [ -z "${CPU}" ]; then
  echo "CPU not set"
  exit 1
fi

if [ -z "${BATCH_SAMPLE}" ]; then
  echo "BATCH_SAMPLE not set"
  exit 1
fi

if [ -z "${BATCH_S3_BUCKET_SAMPLE}" ]; then
  echo "BATCH_S3_BUCKET_SAMPLE not set. No object to download."
  exit 1
fi

if [ -z "${BATCH_S3_BUCKET_CDD}" ]; then
  echo "BATCH_S3_BUCKET_CDD not set. No object to download."
  exit 1
fi

cd /data

echo "Setting AWS credentials"
aws2 configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}
aws2 configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}

echo "Creating working dir"
mkdir -v /data/${BATCH_SAMPLE}
echo "Copying CDD blast database"
time aws2 s3 cp --recursive s3://${BATCH_S3_BUCKET_CDD}/cdd /data/

echo "Copying BlastDB"
time ( curl -sf https://s3.amazonaws.com/ncbi-dev-blast-data/COLO/MANIFEST | egrep 'nt|nr' | egrep -v 'idxn|_v5|piglist' | sed 's,s3://,https://s3.amazonaws.com/,' | parallel -j ${CPU} -t curl -Osf {} )

echo "Copying sample fasta"
time aws2 s3 cp s3://${BATCH_S3_BUCKET_SAMPLE}/${BATCH_SAMPLE}.fa /data/

echo "Running CWL workflow"
time cwltool --no-container --on-error continue --tmpdir-prefix /data/ --tmp-outdir-prefix /data/ --outdir /data/${BATCH_SAMPLE} /home/nobody/cwl-ngs-workflows-cbb/workflows/Annotation/transcriptome_annotation.cwl --blast_db_dir /data --threads ${CPU} --evalue 1e-5 --blast_nt_db nt --blast_nr_db nr --blast_cdd_db cdd --fasta /data/${BATCH_SAMPLE}.fa

echo "Copying results to the S3"
time aws2 s3 cp --recursive /data/${BATCH_SAMPLE} s3://${BATCH_S3_BUCKET_SAMPLE}/

exit 0