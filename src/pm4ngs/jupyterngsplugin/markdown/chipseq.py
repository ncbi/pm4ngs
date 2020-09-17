import itertools
import os

from pm4ngs.jupyterngsplugin.markdown.utils import get_link_image
from pm4ngs.jupyterngsplugin.markdown.utils import get_link_name
from pm4ngs.jupyterngsplugin.markdown.utils import get_link_text
from pm4ngs.jupyterngsplugin.utils.count_lines import count_lines


def diffbind_table(sample_table, result_dir, width, height):
    """
    Diffbid report table
    :param output_suffix: Result path
    :param width: Image width
    :param height: Image height
    :return: string
    """
    comparisons = []
    for s in itertools.combinations(sample_table['condition'].unique(), 2):
        comparisons.append(list(s))
    str_msg = ''
    for c in comparisons:
        comp = '{0}_vs_{1}'.format(c[0], c[1])
        str_msg += '### Condition: {0} vs {1}\n\n'.format(c[0], c[1])
        str_msg += '| Deseq2 | EdgeR |\n'
        str_msg += '| --- | --- |\n'
        f1 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_deseq2_plot.png'))
        f2 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_edgeR_plot.png'))
        str_msg += '| ' + get_link_image(f1, width, height, ' --- ')
        str_msg += '| ' + get_link_image(f2, width, height, ' --- ')
        str_msg += '|\n'
        f1 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_deseq2_plotHeatmap.png'))
        f2 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_edgeR_plotHeatmap.png'))
        str_msg += '| ' + get_link_image(f1, width, height, ' --- ')
        str_msg += '| ' + get_link_image(f2, width, height, ' --- ')
        str_msg += '|\n'
        f1 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_deseq2_plotMA.png'))
        f2 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_edgeR_plotMA.png'))
        str_msg += '| ' + get_link_image(f1, width, height, ' --- ')
        str_msg += '| ' + get_link_image(f2, width, height, ' --- ')
        str_msg += '|\n'
        f1 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_deseq2_plotVolcano.png'))
        f2 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_edgeR_plotVolcano.png'))
        str_msg += '| ' + get_link_image(f1, width, height, ' --- ')
        str_msg += '| ' + get_link_image(f2, width, height, ' --- ')
        str_msg += '|\n'
        f1 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_deseq2_plotPCA.png'))
        f2 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_edgeR_plotPCA.png'))
        str_msg += '| ' + get_link_image(f1, width, height, ' --- ')
        str_msg += '| ' + get_link_image(f2, width, height, ' --- ')
        str_msg += '|\n'
        f1 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_deseq2_plotPCA_contrast.png'))
        f2 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_edgeR_plotPCA_contrast.png'))
        str_msg += '| ' + get_link_image(f1, width, height, ' --- ')
        str_msg += '| ' + get_link_image(f2, width, height, ' --- ')
        str_msg += '|\n'
        f1 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_deseq2_plotBox.png'))
        f2 = os.path.relpath(os.path.join(result_dir, 'condition_'
                                          + comp + '_diffbind_edgeR_plotBox.png'))
        str_msg += '| ' + get_link_image(f1, width, height, ' --- ')
        str_msg += '| ' + get_link_image(f2, width, height, ' --- ')
        str_msg += '|\n\n'

    return str_msg


def peak_calling_table_with_qc(factors, alignment_path, peak_calling_path, width, height):
    """
    Create a peck calling table with phantompeakqualtools plots
    :param factors: Pandas DataFrame with the samples and conditions
    :param alignment_path: Path to the alignments results
    :param peak_calling_path: Path to the peak calling results
    :param width: Image width
    :param height: Image height
    :return: An string in markdown language
    """
    conditions = factors['condition'].unique()
    n_max_samples = 0
    for c in conditions:
        rep = factors[factors['condition'] == c]['sample_name']
        if len(rep) > n_max_samples:
            n_max_samples = len(rep)

    str_msg = '| Condition '
    str_msg += '| No. Peaks '
    for i in range(0, n_max_samples):
        str_msg += '| Sample {0} '.format(i)
    str_msg += '|\n'
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '|\n'

    for c in conditions:
        str_msg += '| ' + c
        str_msg += '| '
        r0 = os.path.relpath(os.path.join(peak_calling_path, c + '_R0_peaks.narrowPeak'))
        if os.path.exists(r0) and os.path.getsize(r0) != 0:
            str_msg += get_link_text(r0, count_lines(r0, '#'), ' --- ')
            str_msg += '|'
        else:
            str_msg += ' --- |'
        rep = factors[factors['condition'] == c]['sample_name']
        for r in rep:
            f = os.path.relpath(os.path.join(alignment_path, r + '_sorted.tagAlign.cc.plot.pdf'))
            str_msg += get_link_image(f, width, height, ' --- ')
            str_msg += '|'
        if len(rep) < n_max_samples:
            for i in range(len(rep), n_max_samples):
                str_msg += ' --- |'
        str_msg += '\n'
    str_msg += '\n'
    str_msg += '\nClick on figure to retrieve original PDF file\n\n'

    return str_msg


def idr_table(factors, idr_path, width, height):
    str_msg = ''
    for c in factors['condition'].unique():
        str_msg += '\n## Condition: {0}\n\n'.format(c)
        f = os.path.relpath(os.path.join(idr_path, c + '.narrowPeak_annotation.txt'))
        str_msg += 'Annotated peak file: '
        str_msg += get_link_name(f, ifempty="")
        str_msg += '\n\nIDR peaks: ' + str(count_lines(f, '#'))
        str_msg += '\n\n| Default  peaks | No alternate<br>summit peaks |\n'
        str_msg += '| --- | --- |\n'
        f = os.path.relpath(os.path.join(idr_path, c + '.narrowPeak.png'))
        str_msg += ' | ' + get_link_image(f, width, height, ' --- ')
        f = os.path.relpath(os.path.join(idr_path, c + '.narrowPeak.noalternatesummitpeaks.png'))
        str_msg += ' | ' + get_link_image(f, width, height, ' --- ')
        str_msg += ' |\n\n'

    return str_msg
