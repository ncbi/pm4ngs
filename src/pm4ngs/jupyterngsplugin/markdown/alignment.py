import os
import numpy as np
import matplotlib.pyplot as plt

from pm4ngs.jupyterngsplugin.markdown.utils import find_file_print_link_size, get_link_size
from pm4ngs.jupyterngsplugin.utils.load_content_dict import load_content_dict
from pm4ngs.jupyterngsplugin.utils.load_content_dict import load_content_dict_line


def star_alignment_table_single(samples_data, sample_list, alignment_path):
    """
    Print alignment report table parsing data from STAR
    :param samples_data: Dict returned from fastqc_trimmomatic_table with extracted data
    :param sample_list: list of samples prefix names
    :param alignment_path: Folder to alignment results
    :return: Dict with samples data and the table in string format
    """
    str_msg = '| Sample | Sorted<br>BAM | BAM<br>Index | STATS'
    str_msg += '| Number<br>of input<br>reads | Uniquely<br>mapped<br>reads % '
    str_msg += '| % of reads<br>mapped to<br>multiple<br>loci '
    str_msg += '| Number of<br>splices:<br>Annotated<br>(sjdb) '
    str_msg += '| Mismatch<br>rate per<br>base, % '
    str_msg += '|\n| --- | --- | --- | --- '
    str_msg += '| --- | --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '| --- '
    str_msg += '|\n'
    for s in sample_list:
        str_msg += '| ' + s + ' | '
        str_msg += find_file_print_link_size(alignment_path, s, '_sorted.bam', 'MB', ' --- ')
        str_msg += ' |'
        str_msg += find_file_print_link_size(alignment_path, s, '_sorted.bam.bai', 'MB', ' --- ')
        str_msg += ' |'
        files = [f for ds, dr, files in os.walk(alignment_path) for f in files if
                 f.startswith(s) and f.endswith('Log.final.out')
                 and os.path.getsize(os.path.join(alignment_path, f)) != 0]
        if len(files) == 1:
            f = os.path.relpath(os.path.join(alignment_path, files[0]))
            str_msg += get_link_size(f, 'KB', ' --- ')
            str_msg += ' |'
            stats = load_content_dict(f, '\t', True, ' |', '')
            samples_data[s]['alignment'] = {
                'unique': int(stats['Uniquely mapped reads number']),
                'multiple': int(stats['Number of reads mapped to multiple loci']),
                'unmapped':
                    int(stats['Number of input reads'])
                    - (int(stats['Uniquely mapped reads number'])
                       + int(stats['Number of reads mapped to multiple loci']))
            }
            str_msg += "{:,}".format(
                int(stats['Number of input reads'])) + ' |'
            str_msg += "{0:.2f}".format(
                float(stats['Uniquely mapped reads %'].replace('%', ''))) + ' |'
            str_msg += "{0:.2f}".format(
                float(stats['% of reads mapped to multiple loci'].replace('%', ''))) + ' |'
            str_msg += "{:,}".format(
                int(stats['Number of splices: Annotated (sjdb)'])) + ' |'
            str_msg += "{0:.2f}".format(
                float(stats['Mismatch rate per base, %'].replace('%', ''))) + ' |'
            str_msg += '\n'
        else:
            str_msg += ' --- | --- | --- | --- |\n'
    return samples_data, str_msg


def samtools_stat_alignment_table_paired(samples_data, sample_list, alignment_path):
    """
    Print alignment report table parsing data from samtools stats
    :param samples_data: Dict returned from fastqc_trimmomatic_table with extracted data
    :param sample_list: list of samples prefix names
    :param alignment_path: Folder to alignment results
    :return: Dict with samples data and the table in string format
    """
    str_msg = '| Sample | Sorted<br>BAM | BAM<br>Index | STATS'
    str_msg += '| Mapped<br>reads | Un-Mapped<br>reads | Properly<br>paired<br>reads (%) '
    str_msg += '| Total<br>first<br>fragment<br>length '
    str_msg += '| Bases<br>mapped '
    str_msg += '| Bases<br>mapped<br>(cigar) '
    str_msg += '| Mismatches '
    str_msg += '| Error<br>rate '
    str_msg += '| Average<br>length '
    str_msg += '| Average<br>quality '
    str_msg += '|\n| --- | --- | --- | --- '
    str_msg += '| --- | --- '
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
        str_msg += find_file_print_link_size(alignment_path, s, '_sorted.bam',
                                             'MB', ' --- ')
        str_msg += ' |'
        str_msg += find_file_print_link_size(alignment_path, s, '_sorted.bam.bai',
                                             'MB', ' --- ')
        str_msg += ' |'
        files = [f for ds, dr, files in os.walk(alignment_path) for f in files if
                 f.startswith(s) and f.endswith('.stats')
                 and os.path.getsize(os.path.join(alignment_path, f)) != 0]
        if len(files) == 1:
            f = os.path.relpath(os.path.join(alignment_path, files[0]))
            str_msg += get_link_size(f, 'KB', ' --- ')
            str_msg += ' |'
            stats = load_content_dict_line(f, ':', 'SN', '\t', True, 'SN\t', '')
            if s not in samples_data:
                samples_data[s] = {}
            samples_data[s]['alignment'] = {
                'mapped': int(stats['reads mapped']),
                'unmapped': int(stats['reads unmapped']),
                'properly paired': int(stats['reads properly paired'])
            }
            str_msg += "{:,}".format(int(stats['reads mapped'])) + ' |'
            str_msg += "{:,}".format(int(stats['reads unmapped'])) + ' |'
            str_msg += "{:,}".format(float(stats['percentage of properly paired reads (%)']))
            str_msg += ' |'
            str_msg += "{:,}".format(int(stats['total first fragment length'])) + ' |'
            str_msg += "{:,}".format(int(stats['bases mapped'])) + ' |'
            str_msg += "{:,}".format(int(stats['bases mapped (cigar)'].replace('%', ''))) + ' |'
            str_msg += "{:,}".format(int(stats['mismatches'].replace('%', ''))) + ' |'
            str_msg += "{:.2e}".format(float(stats['error rate'].replace('%', ''))) + ' |'
            str_msg += "{:,}".format(int(stats['average length'].replace('%', ''))) + ' |'
            str_msg += "{:.1f}".format(float(stats['average quality'].replace('%', ''))) + ' |'
            str_msg += '\n'
        else:
            str_msg += ' --- | --- | --- | --- |\n'
    return samples_data, str_msg


def samtools_stat_alignment_table_single(samples_data, sample_list, alignment_path):
    """
    Print alignment report table parsing data from samtools stats
    :param samples_data: Dict returned from fastqc_trimmomatic_table with extracted data
    :param sample_list: list of samples prefix names
    :param alignment_path: Folder to alignment results
    :return: Dict with samples data and the table in string format
    """
    str_msg = '| Sample | Sorted<br>BAM | BAM<br>Index | STATS'
    str_msg += '| Mapped<br>reads | Un-Mapped<br>reads '
    str_msg += '| Total<br>first<br>fragment<br>length '
    str_msg += '| Bases<br>mapped '
    str_msg += '| Bases<br>mapped<br>(cigar) '
    str_msg += '| Mismatches '
    str_msg += '| Error<br>rate '
    str_msg += '| Average<br>length '
    str_msg += '| Average<br>quality '
    str_msg += '|\n| --- | --- | --- | --- '
    str_msg += '| --- | --- '
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
        str_msg += find_file_print_link_size(alignment_path, s, '_sorted.bam',
                                             'MB', ' --- ')
        str_msg += ' |'
        str_msg += find_file_print_link_size(alignment_path, s, '_sorted.bam.bai',
                                             'MB', ' --- ')
        str_msg += ' |'
        f = os.path.relpath(os.path.join(alignment_path, s + '.stats'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            str_msg += get_link_size(f, 'KB', ' --- ')
            str_msg += ' |'
            stats = load_content_dict_line(f, ':', 'SN', '\t', True, 'SN\t', '')
            if s not in samples_data:
                samples_data[s] = {}
            samples_data[s]['alignment'] = {
                'mapped': int(stats['reads mapped']),
                'unmapped': int(stats['reads unmapped'])
            }
            str_msg += "{:,}".format(int(stats['reads mapped'])) + ' |'
            str_msg += "{:,}".format(int(stats['reads unmapped'])) + ' |'
            str_msg += "{:,}".format(int(stats['total first fragment length'])) + ' |'
            str_msg += "{:,}".format(int(stats['bases mapped'])) + ' |'
            str_msg += "{:,}".format(int(stats['bases mapped (cigar)'].replace('%', ''))) + ' |'
            str_msg += "{:,}".format(int(stats['mismatches'].replace('%', ''))) + ' |'
            str_msg += "{:.2e}".format(float(stats['error rate'].replace('%', ''))) + ' |'
            str_msg += "{:,}".format(int(stats['average length'].replace('%', ''))) + ' |'
            str_msg += "{:.1f}".format(float(stats['average quality'].replace('%', ''))) + ' |'
            str_msg += '\n'
        else:
            str_msg += ' --- | --- | --- | --- |\n'
    return samples_data, str_msg


def alignment_table(samples_data, sample_list, alignment_path, alignment_tool):
    """
Print alignment report table parsing data from STAR
    :param samples_data: Dict returned from fastqc_trimmomatic_table with extracted data
    :param sample_list: list of samples prefix names
    :param alignment_path: Folder to alignment results
    :param alignment_tool: Tools used for the alignment
    :return:Dict with samples data and the table in string format
    """
    if alignment_tool == 'STAR_single':
        return star_alignment_table_single(samples_data, sample_list, alignment_path)
    elif alignment_tool == 'BWA_paired' or alignment_tool == 'STAR_paired':
        return samtools_stat_alignment_table_paired(samples_data, sample_list, alignment_path)
    elif alignment_tool == 'BWA_single':
        return samtools_stat_alignment_table_single(samples_data, sample_list, alignment_path)


def star_reads_distribution_plot_single(samples_data, sample_list, fig_size):
    """
    Create the distribution of reads plot for single-end data
    :param samples_data: Dict returned from alignment_table with extracted data
    :param sample_list: list of samples prefix names
    :param fig_size: Tuple with figure size
    :return: matplotlib plot
    """
    f, plot = plt.subplots(figsize=fig_size)
    N = 0
    unique = []
    multiple = []
    unmapped = []
    trimmed = []
    for s in sample_list:
        if 'alignment' in samples_data[s]:
            N += 1
            unique.append(samples_data[s]['alignment']['unique'])
            multiple.append(samples_data[s]['alignment']['multiple'])
            unmapped.append(samples_data[s]['alignment']['unmapped'])
            trimmed.append(
                samples_data[s]['fastqc']['tot_seq'] - samples_data[s]['trimmed']['tot_seq'])
    ind = np.arange(N)
    width = 0.45

    p4 = plot.bar(ind, trimmed, width, color='#2eea15')
    p3 = plot.bar(ind, unmapped, width,
                  bottom=np.array(trimmed), color='#ea1563')
    p2 = plot.bar(ind, multiple, width,
                  bottom=np.array(trimmed) + np.array(unmapped), color='#ff7311')
    p1 = plot.bar(ind, unique, width,
                  bottom=np.array(trimmed) + np.array(unmapped) + np.array(multiple),
                  color='#1c6cab')

    plt.ylabel('No. of Reads')
    plt.xticks(ind, sample_list, rotation='vertical')
    plt.legend((p1[0], p2[0], p3[0], p4[0]),
               ('Unique Mapped', 'Multiple Mapped', 'Unmapped', 'Trimmed'))

    return plot


def star_reads_distribution_plot_paired(samples_data, sample_list, fig_size):
    """
    Create the distribution of reads plot for paired-end data
    :param samples_data: Dict returned from alignment_table with extracted data
    :param sample_list: list of samples prefix names
    :param fig_size: Tuple with figure size
    :return: matplotlib plot
    """
    f, plot = plt.subplots(figsize=fig_size)
    N = 0
    mapped = []
    unmapped = []
    for s in sample_list:
        if s in samples_data:
            if 'alignment' in samples_data[s]:
                N += 1
                mapped.append(samples_data[s]['alignment']['properly paired'])
                unmapped.append(samples_data[s]['alignment']['unmapped'])
    ind = np.arange(N)
    width = 0.50

    p2 = plot.bar(ind, unmapped, width, color='#ea1563')
    p1 = plot.bar(ind, mapped, width, bottom=np.array(unmapped), color='#1c6cab')

    plt.ylabel('No. of Reads')
    plt.xticks(ind, sample_list, rotation='vertical')
    plt.legend((p1[0], p2[0]), ('Properly paired', 'Unmapped'))

    return plot


def samtools_reads_distribution_plot_single(samples_data, sample_list, fig_size):
    """
    Create the distribution of reads plot from Samtools stats
    :param samples_data: Dict returned from alignment_table with extracted data
    :param sample_list: list of samples prefix names
    :param fig_size: Tuple with figure size
    :return: matplotlib plot
    """
    f, plot = plt.subplots(figsize=fig_size)
    N = 0
    mapped = []
    unmapped = []
    trimmed = []
    for s in sample_list:
        if 'alignment' in samples_data[s]:
            N += 1
            mapped.append(samples_data[s]['alignment']['mapped'])
            unmapped.append(samples_data[s]['trimmed']['tot_seq'] -
                            samples_data[s]['alignment']['mapped'])
            trimmed.append(samples_data[s]['fastqc']['tot_seq'] -
                           samples_data[s]['trimmed']['tot_seq'])
    ind = np.arange(N)
    width = 0.45

    p3 = plot.bar(ind, trimmed, width, color='#2eea15')
    p2 = plot.bar(ind, unmapped, width,
                  bottom=np.array(trimmed), color='#ea1563')
    p1 = plot.bar(ind, mapped, width,
                  bottom=np.array(trimmed) + np.array(unmapped), color='#1c6cab')

    plt.ylabel('No. of Reads')
    plt.xticks(ind, sample_list, rotation='vertical')
    plt.legend((p1[0], p2[0], p3[0]),
               ('Mapped', 'Unmapped', 'Trimmed'))

    return plot


def samtools_reads_distribution_plot_paired(samples_data, sample_list, fig_size):
    """
    Create the distribution of reads plot from Samtools stats
    :param samples_data: Dict returned from alignment_table with extracted data
    :param sample_list: list of samples prefix names
    :param fig_size: Tuple with figure size
    :return: matplotlib plot
    """
    f, plot = plt.subplots(figsize=fig_size)
    N = 0
    mapped = []
    ppaired = []
    unmapped = []
    for s in sample_list:
        if 'alignment' in samples_data[s] and 'properly paired' in samples_data[s]['alignment']:
            N += 1
            mapped.append(samples_data[s]['alignment']['mapped'])
            unmapped.append(samples_data[s]['alignment']['unmapped'])
            ppaired.append(samples_data[s]['alignment']['properly paired'])
    ind = np.arange(N)
    width = 0.45

    p3 = plot.bar(ind, unmapped, width, color='#2eea15')
    p2 = plot.bar(ind, ppaired, width,
                  bottom=np.array(unmapped), color='#ea1563')
    p1 = plot.bar(ind, mapped, width,
                  bottom=np.array(unmapped) + np.array(ppaired), color='#1c6cab')

    plt.ylabel('No. of Reads')
    plt.xticks(ind, sample_list, rotation='vertical')
    plt.legend((p1[0], p2[0], p3[0]),
               ('Mapped', 'Properly paired', 'Unmapped'))

    return plot


def reads_distribution_plot(samples_data, sample_list, fig_size, alignment_tool):
    """
    Create the distribution of reads plot
    :param samples_data: Dict returned from alignment_table with extracted data
    :param sample_list: list of samples prefix names
    :param fig_size: Tuple with figure size
    :param alignment_tool: Tools used for the alignment
    :return: matplotlib plot
    """
    if alignment_tool == 'STAR_single':
        return star_reads_distribution_plot_single(samples_data, sample_list, fig_size)
    elif alignment_tool == 'STAR_paired':
        return star_reads_distribution_plot_paired(samples_data, sample_list, fig_size)
    elif alignment_tool == 'BWA_single':
        return samtools_reads_distribution_plot_single(samples_data, sample_list, fig_size)
    elif alignment_tool == 'BWA_paired':
        return samtools_reads_distribution_plot_paired(samples_data, sample_list, fig_size)
