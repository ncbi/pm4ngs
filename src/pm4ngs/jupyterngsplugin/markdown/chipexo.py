import os

import pandas

from pm4ngs.jupyterngsplugin.markdown.utils import get_link_image
from pm4ngs.jupyterngsplugin.markdown.utils import get_link_text
from pm4ngs.jupyterngsplugin.utils.count_lines import count_lines


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
        r0 = os.path.relpath(os.path.join(peak_calling_path, c + '.border_pair_annot.bed'))
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


def meme_motif_table_condition(motif_path, c, d, width, height):
    str_msg = ''
    f = os.path.relpath(os.path.join(motif_path, c + '.border_pair_annot_' + d,
                                     'summary.tsv'))
    if os.path.exists(f) and os.path.getsize(f) != 0:
        df = pandas.read_csv(f, sep='\t', comment='#')
        if not df.empty:
            n_motif = len(df)
            source = df.iloc[0]['MOTIF_SOURCE']
            consensus = df.iloc[0]['CONSENSUS']
            w = df.iloc[0]['WIDTH']
            sites = df.iloc[0]['SITES']
            e_value = df.iloc[0]['E-VALUE']
            lhtml = os.path.relpath(os.path.join(motif_path, c + '.border_pair_annot_' + d,
                                                 'meme-chip.html'))
            str_msg += '| ' + get_link_text(lhtml, c, ' --- ')
            str_msg += '|'

            str_msg += " {} | {} | {} | {} | {} | {} | ".format(n_motif, source, consensus,
                                                                w, sites, e_value)
            if source == 'MEME':
                lpng = os.path.relpath(
                    os.path.join(motif_path, c + '.border_pair_annot_' + d, 'meme_out',
                                 'logo1.png'))
                if os.path.exists(lpng) and os.path.getsize(lpng) != 0:
                    str_msg += get_link_image(lpng, width, height, ' --- ')
                    str_msg += ' |'
                else:
                    str_msg += ' --- |'
            elif source == 'DREME':
                lout = os.path.relpath(os.path.join(motif_path, c
                                                    + '.border_pair_annot_'
                                                    + d,
                                                    'dreme_out'))
                dreme_files = [f for ds, dr, files in os.walk(lout)
                               for f in files if f.startswith('m01nc')]
                for dm in dreme_files:
                    loutfile = os.path.relpath(
                        os.path.join(motif_path, c + '.border_pair_annot_' + d,
                                     'dreme_out', dm))
                    if os.path.exists(loutfile) and os.path.getsize(loutfile) != 0:
                        str_msg += get_link_image(loutfile, width, height, ' --- ')
                        str_msg += ' |'
                    else:
                        str_msg += ' --- |'
            str_msg += '\n'
    return str_msg


def meme_motif_table(factors, motif_path, width, height):
    """
    Create a table for the MEME motif find results
    :param factors: Pandas DataFrame with the samples and conditions
    :param motif_path: Path to the MEME results
    :param width: Image width
    :param height: Image height
    :return: An string in markdown language
    """
    conditions = factors['condition'].unique()
    memedbs = []
    dirs = [d for d in os.listdir(motif_path) if os.path.isdir(os.path.join(motif_path, d))]
    for d in dirs:
        if '.border_pair_annot_' in d:
            d = d.split('.border_pair_annot_')[1]
            memedbs.append(d)
    memedbs = list(set(memedbs))
    str_msg = ""
    for d in memedbs:
        str_msg += "### Database: {}\n\n".format(d)
        str_msg += "| Sample/<br>MEME output | No.<br>Motifs | 1st motif<br>source "
        str_msg += "| 1st motif<br>consensus | 1st motif<br>width | 1st motif<br>sites "
        str_msg += "| 1st motif<br>E-Value | 1st motif |\n"
        str_msg += "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        for c in conditions:
            str_msg += meme_motif_table_condition(motif_path, c, d, width, height)
        str_msg += '\n\n\n'
    return str_msg
