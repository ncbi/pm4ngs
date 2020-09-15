import os

from pm4ngs.jupyterngsplugin.utils.yaml_utils import write_to_yaml


def write_sample_table_pe_to_yaml(sample_table, data_dir, file_name):
    samples = []
    for i, r in sample_table.iterrows():
        sample = []
        if not r['file']:
            r1 = os.path.join(data_dir, r['sample_name'] + '_1.fastq.gz')
            r2 = os.path.join(data_dir, r['sample_name'] + '_2.fastq.gz')
            sample.append({'class': 'File', 'path': r1})
            sample.append({'class': 'File', 'path': r2})
        else:
            for f in r['file'].split(','):
                sample.append({'class': 'File', 'path': r1})
        samples.append(sample)
    write_to_yaml(samples, file_name)


def write_sample_table_se_to_yaml(sample_table, data_dir, file_name):
    samples = []
    for i, r in sample_table.iterrows():
        if not r['file']:
            r = os.path.join(data_dir, r['sample_name'] + '.fastq.gz')
            samples.append({'class': 'File', 'path': r})
        else:
            samples.append({'class': 'File', 'path': r['file']})
    write_to_yaml(samples, file_name)
