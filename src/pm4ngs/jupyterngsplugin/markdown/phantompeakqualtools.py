import os
from pm4ngs.jupyterngsplugin.markdown.utils import get_link_image


def print_table_cell(f):
    str_msg = ''
    with open(f) as fin:
        for line in fin:
            fields = line.strip().split('\t')
            str_msg += "{:.2e}".format(float(fields[1])) + ' |'

            for i in fields[2].split(','):
                str_msg += "{:,}".format(int(i)) + '<br>'
            str_msg += ' |'

            for i in fields[3].split(','):
                str_msg += "{:.2f}".format(float(i)) + '<br>'
            str_msg += ' |'

            str_msg += fields[4] + ' |'
            str_msg += "{:.2f}".format(float(fields[5])) + ' |'

            str_msg += fields[6] + ' |'

            str_msg += "{:.2f}".format(float(fields[7])) + ' |'
            if float(fields[8]) < 1.05:
                str_msg += '<font color=\'red\'>'
            str_msg += "{:.2f}".format(float(fields[8]))
            if float(fields[8]) < 1.05:
                str_msg += '</font>'
            str_msg += ' |'
            if float(fields[9]) < 0.8:
                str_msg += '<font color=\'red\'>'
            str_msg += "{:.2f}".format(float(fields[9]))
            if float(fields[9]) < 0.8:
                str_msg += '</font>'
            str_msg += ' |'
            try:
                str_msg += "{:.2f}".format(float(fields[10])) + ' |'
            except ValueError:
                str_msg += ' --- |'
    return str_msg


def qc_table(sample_list, alignment_path, width, height):
    str_msg = '| Sample '
    str_msg += '| numReads '
    str_msg += '| estFragLen '
    str_msg += '| corr_estFragLen '
    str_msg += '| phantomPeak '
    str_msg += '| corr_phantomPeak '
    str_msg += '| argmin_corr '
    str_msg += '| min_corr '
    str_msg += '| NSC '
    str_msg += '| RSC '
    str_msg += '| QualityTag '
    str_msg += '| strand-shift cc '
    str_msg += '|\n| --- | --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '|\n'
    for s in sample_list:
        str_msg += '| ' + s
        str_msg += '| '
        f = os.path.relpath(os.path.join(alignment_path, s + '_sorted.tagAlign.cc.qc'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            str_msg += print_table_cell(f)
        else:
            str_msg += ' --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |'
        f = os.path.relpath(os.path.join(alignment_path, s + '_sorted.tagAlign.cc.plot.pdf'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            str_msg += get_link_image(f, width, height, ' --- |\n')
        else:
            str_msg += ' --- |'
        str_msg += '\n'
    str_msg += '\n'
    return str_msg
