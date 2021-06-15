import os

from pm4ngs.jupyterngsplugin.image.pdftobase64 import pdftobase64
from pm4ngs.jupyterngsplugin.utils.load_content_dict import load_content_dict


def rseqc_plot_table(sample_list, data_path, width, height):
    """

    :param sample_list: list of samples prefix names
    :param data_path:
    :param width:
    :param height:
    :return:
    """
    str_msg = 'Click on figure to retrieve original PDF file\n\n'
    str_msg += '| Sample | Splice Events | Junction Saturation '
    str_msg += '|\n| --- | --- | --- '
    str_msg += '|\n'
    for s in sample_list:
        str_msg += '| ' + s
        str_msg += '| '
        files = [f for ds, dr, files in os.walk(data_path) for f in files if
                 f.startswith(s) and f.endswith('rseqc.splice_events.pdf')
                 and os.path.getsize(os.path.join(data_path, f)) != 0]
        if len(files) == 1:
            f = os.path.relpath(os.path.join(data_path, files[0]))
            str_msg += ' <a href="'
            str_msg += f.replace(' ', '%20')
            str_msg += '" target="_blank">'
            str_msg += '<img src="data:image/png;base64,' + pdftobase64(f, width, height) + '">'
            str_msg += '</a> |'
        else:
            str_msg += ' --- |'
        files = [f for ds, dr, files in os.walk(data_path) for f in files if
                 f.startswith(s) and f.endswith('rseqc.junctionSaturation_plot.pdf')
                 and os.path.getsize(os.path.join(data_path, f)) != 0]
        if len(files) == 1:
            f = os.path.relpath(os.path.join(data_path, files[0]))
            str_msg += ' <a href="'
            str_msg += f.replace(' ', '%20')
            str_msg += '" target="_blank">'
            str_msg += '<img src="data:image/png;base64,' + pdftobase64(f, width, height) + '">'
            str_msg += '</a> |'
        else:
            str_msg += ' --- |'
        str_msg += '\n'
    return str_msg


def rseqc_table(sample_list, data_path):
    """
    Create RseQC report table
    :param sample_list: list of samples prefix names
    :param data_path: Folder with RseQC outputs
    :return:
    """
    str_msg = '| Sample | Total records | QC failed | Optical/PCR duplicate '
    str_msg += '| mapq < mapq_cut (non-unique) | mapq >= mapq_cut (unique) '
    str_msg += '| Reads map to \'+\' '
    str_msg += '| Reads map to \'-\' '
    str_msg += '| Non-splice reads '
    str_msg += '| Splice reads '
    str_msg += '|\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- '
    str_msg += '|\n'
    for s in sample_list:
        str_msg += '| ' + s
        str_msg += '| '

        files = [f for ds, dr, files in os.walk(data_path) for f in files if
                 f.startswith(s) and f.endswith('.bam_stat.txt')
                 and os.path.getsize(os.path.join(data_path, f)) != 0]
        if len(files) == 1:
            f = os.path.relpath(os.path.join(data_path, files[0]))
            stats = load_content_dict(f, ':', True)
            str_msg += "{:,}".format(int(stats['Total records'])) + ' |'
            str_msg += "{:,}".format(int(stats['QC failed'])) + ' |'
            str_msg += "{:,}".format(int(stats['Optical/PCR duplicate'])) + ' |'
            str_msg += "{:,}".format(int(stats['mapq < mapq_cut (non-unique)'])) + ' |'
            str_msg += "{:,}".format(int(stats['mapq >= mapq_cut (unique)'])) + ' |'
            str_msg += "{:,}".format(int(stats['Reads map to \'+\''])) + ' |'
            str_msg += "{:,}".format(int(stats['Reads map to \'-\''])) + ' |'
            str_msg += "{:,}".format(int(stats['Non-splice reads'])) + ' |'
            str_msg += "{:,}".format(int(stats['Splice reads'])) + ' |'
        else:
            str_msg += ' | --- | --- | --- | --- | --- | --- | --- | --- | --- '
        str_msg += '\n'
    return str_msg
