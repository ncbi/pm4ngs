import os

from pm4ngs.jupyterngsplugin.files.fastq.fastqc import parse_fastqc_zip
from pm4ngs.jupyterngsplugin.markdown.utils import find_file_print_link_size


def fastqc_table(sample_list, samples_path, fastqc_path):
    """
    Print FastQC report table parsing data
    :param sample_list: list of samples prefix names
    :param samples_path: Path to original fastq files
    :param fastqc_path: Path to FastQC output folder
    :return: Dict with samples data and the table in string format
    """
    samples_data = {}
    str_msg = '| Sample | Fastq | FastQC<br>Report | No of Reads<br>in fastq | Seq<br> Len | %GC '
    str_msg += '| Poor<br>Quality | Fail<br>Tests |\n'
    str_msg += '| --- | --- | --- |--- | --- | --- | --- | --- |\n'
    for s in sample_list:
        str_msg += '| ' + s
        str_msg += '| '
        str_msg += find_file_print_link_size(samples_path, s, '.fastq.gz', 'MB', ' --- ')
        str_msg += ' |'
        str_msg += find_file_print_link_size(fastqc_path, s, '.html', 'MB', ' --- ')
        str_msg += ' |'
        f = os.path.relpath(os.path.join(fastqc_path, s + '_fastqc.zip'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            tests, tot_seq, poor_quality, seq_len, gc_content = parse_fastqc_zip(f)
            samples_data[s] = {'fastqc': {
                'tests': tests,
                'tot_seq': tot_seq,
                'poor_quality': poor_quality,
                'seq_len': seq_len,
                'gc_content': gc_content
            }
            }
            str_msg += "{:,}".format(tot_seq) + '|'
            str_msg += seq_len + '|'
            str_msg += gc_content + '|'
            str_msg += str(poor_quality) + '|'
            fail_tests = ''
            for t in tests:
                if tests[t] == 'FAIL':
                    if fail_tests:
                        fail_tests += '<br>'
                    fail_tests += t
            str_msg += fail_tests + '|\n'

        else:
            str_msg += ' --- | --- | --- | --- | --- |\n'
    return samples_data, str_msg


def fastqc_trimmomatic_table(samples_data, sample_list, trimmomatic_path):
    """
    Print FastQC report table parsing data for trimmed samples
    :param samples_data: Dict returned from fastqc_table with extracted data
    :param sample_list: list of samples prefix names
    :param trimmomatic_path: Folder with trimmed samples and FastQC reports
    :return: Dict with samples data and the table in string format
    """
    str_msg = '| Sample | Trimmed<br>Fastq | FastQC<br>Report | No of Reads<br>in fastq |'
    str_msg += 'Removed<br>Reads | Seq<br> Len | %GC | Poor<br>Quality | Fail<br>Tests |\n'
    str_msg += '| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n'
    for s in sample_list:
        str_msg += '| ' + s
        str_msg += '| '
        str_msg += find_file_print_link_size(trimmomatic_path, s, '.fastq.gz', 'MB', ' --- ')
        str_msg += ' |'
        str_msg += find_file_print_link_size(trimmomatic_path, s, '.html', 'KB', ' --- ')
        str_msg += ' |'
        files = [f for ds, dr, files in os.walk(trimmomatic_path) for f in files if
                 f.startswith(s) and f.endswith('_fastqc.zip')
                 and os.path.getsize(os.path.join(trimmomatic_path, f)) != 0]
        if len(files) == 1:
            f = os.path.relpath(os.path.join(trimmomatic_path, files[0]))
            tests, tot_seq, poor_quality, seq_len, gc_content = parse_fastqc_zip(f)
            str_msg += "{:,}".format(tot_seq) + '|'
            str_msg += "{:,}".format(samples_data[s]['fastqc']['tot_seq'] - tot_seq) + '|'
            str_msg += seq_len + '|'
            str_msg += gc_content + '|'
            str_msg += str(poor_quality) + '|'
            fail_tests = ''
            for t in tests:
                if tests[t] == 'FAIL':
                    if fail_tests:
                        fail_tests += '<br>'
                    fail_tests += t
            str_msg += fail_tests + '|\n'
            samples_data[s]['trimmed'] = {
                'tests': tests,
                'tot_seq': tot_seq,
                'poor_quality': poor_quality,
                'seq_len': seq_len,
                'gc_content': gc_content
            }
        else:
            str_msg += ' --- | --- | --- | --- | --- | --- |\n'
    return samples_data, str_msg
