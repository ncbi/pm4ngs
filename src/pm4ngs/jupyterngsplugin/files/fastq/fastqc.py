import os
import zipfile


def parse_fastqc_zip(zip_file):
    """
    This function extract from a fastQC zip file the failing tests and data
    :param zip_file: FastQC zip file
    :return:
    """
    tests = {}
    tot_seq = 0
    poor_quality = 0
    seq_len = ''
    gc_content = ''
    if os.path.exists(zip_file) and os.path.getsize(zip_file) != 0:
        prefix = os.path.basename(zip_file).replace('.zip', '')
        with zipfile.ZipFile(zip_file) as myzip:
            with myzip.open(prefix + '/summary.txt') as myfile:
                for line in myfile:
                    fields = line.strip().decode('utf8').split('\t')
                    tests[fields[1]] = fields[0]
            with myzip.open(prefix + '/fastqc_data.txt') as myfile:
                for line in myfile:
                    fields = line.strip().decode('utf8').split('\t')
                    if fields[0] == 'Total Sequences':
                        tot_seq = int(fields[1])
                    if fields[0] == 'Sequences flagged as poor quality':
                        poor_quality = int(fields[1])
                    if fields[0] == 'Sequence length':
                        seq_len = fields[1]
                    if fields[0] == '%GC':
                        gc_content = fields[1]
    return tests, tot_seq, poor_quality, seq_len, gc_content
