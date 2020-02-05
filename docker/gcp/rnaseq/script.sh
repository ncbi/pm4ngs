#!/usr/bin/env bash

gcloud beta lifesciences pipelines run --machine-type n1-standard-8  --boot-disk-size 50 \
--command-line 'cwltool --no-container --on-error continue --outdir /gcloud-shared/ https://raw.githubusercontent.com/ncbi/cwl-ngs-workflows-cbb/master/workflows/Alignments/star-alignment-PE.cwl --threads 8 --genomeDir ${INDEX} --reads_1 ${R1} --reads_2 ${R2}' \
--docker-image 'gcr.io/cbb-research-dl/rnaseq-dga' \
--logging gs://cbb-research-dl-life-sciences/SRR2126795_sorted.log \
--inputs I1=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/Genome \
--inputs I2=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/SA \
--inputs I3=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/SAindex \
--inputs I4=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/chrLength.txt \
--inputs I5=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/chrName.txt \
--inputs I6=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/chrNameLength.txt \
--inputs I7=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/chrStart.txt \
--inputs I8=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/exonGeTrInfo.tab \
--inputs I9=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/exonInfo.tab \
--inputs I10=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/geneInfo.tab \
--inputs I11=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/genes.gtf \
--inputs I12=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/genome.fa \
--inputs I13=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/genomeParameters.txt \
--inputs I14=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/sjdbInfo.txt \
--inputs I15=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/sjdbList.fromGTF.out.tab \
--inputs I16=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/sjdbList.out.tab \
--inputs I17=gs://ngs-resources/indexes/STAR-2.7.1a/hg38/transcriptInfo.tab \
--inputs R1=gs://cbb-research-dl-life-sciences/SRR2126795_1.fastq.gz \
--inputs R2=gs://cbb-research-dl-life-sciences/SRR2126795_2.fastq.gz \
--outputs BAM=gs://cbb-research-dl-life-sciences/SRR2126795_sorted.bam \
--outputs BAI=gs://cbb-research-dl-life-sciences/SRR2126795_sorted.bam.bai \
--outputs STATS=gs://cbb-research-dl-life-sciences/SRR2126795Aligned.out.stats \
--outputs LOG=gs://cbb-research-dl-life-sciences/SRR2126795Log.final.out \
--outputs READS=gs://cbb-research-dl-life-sciences/SRR2126795ReadsPerGene.out.tab \
--env-vars=INDEX=/gcloud-shared/,\
R1=/gcloud-shared/SRR2126795_1.fastq.gz,\
R2=/gcloud-shared/SRR2126795_2.fastq.gz,\
I1=/gcloud-shared/Genome,\
I2=/gcloud-shared/SA,\
I3=/gcloud-shared/SAindex,\
I4=/gcloud-shared/chrLength.txt,\
I5=/gcloud-shared/chrName.txt,\
I6=/gcloud-shared/chrNameLength.txt,\
I7=/gcloud-shared/chrStart.txt,\
I8=/gcloud-shared/exonGeTrInfo.tab,\
I9=/gcloud-shared/exonInfo.tab,\
I10=/gcloud-shared/geneInfo.tab,\
I11=/gcloud-shared/genes.gtf,\
I12=/gcloud-shared/genome.fa,\
I13=/gcloud-shared/genomeParameters.txt,\
I14=/gcloud-shared/sjdbInfo.txt,\
I15=/gcloud-shared/sjdbList.fromGTF.out.tab,\
I16=/gcloud-shared/sjdbList.out.tab,\
I17=/gcloud-shared/transcriptInfo.tab,\
BAM=/gcloud-shared/SRR2126795_sorted.bam,\
BAI=/gcloud-shared/SRR2126795_sorted.bam.bai,\
STATS=/gcloud-shared/SRR2126795Aligned.out.stats,\
LOG=/gcloud-shared/SRR2126795Log.final.out,\
READS=/gcloud-shared/SRR2126795ReadsPerGene.out.tab
