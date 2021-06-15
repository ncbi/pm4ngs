import os

import pandas

from pm4ngs.jupyterngsplugin.markdown.utils import get_link_image


def print_tools(c, tools, files, data_path, width, height):
    str_msg = '| '
    for t in tools:
        f = [f for f in files if c + '_' + t + '_volcano.pdf' in f]
        if len(f) == 1:
            f = os.path.relpath(os.path.join(data_path, f[0]))
            str_msg += get_link_image(f, width, height, ' --- ')
            str_msg += ' | '
        else:
            str_msg += '| --- |'
    str_msg += '\n| '
    for t in tools:
        f = [f for f in files if c + '_' + t + '_correlation_heatmap' in f]
        if len(f) == 1:
            f = os.path.relpath(os.path.join(data_path, f[0]))
            str_msg += get_link_image(f, width, height, ' --- ')
            str_msg += ' | '
        else:
            str_msg += ' --- |'
    str_msg += '\n| '
    for t in tools:
        f = [f for f in files if c + '_' + t + '_expression_heatmap.pdf' in f]
        if len(f) == 1:
            f = os.path.relpath(os.path.join(data_path, f[0]))
            str_msg += get_link_image(f, width, height, ' --- ')
            str_msg += ' | '
        else:
            str_msg += ' --- |'
    str_msg += '\n| '
    for t in tools:
        f = [f for f in files if c + '_' + t + '_pca.pdf' in f]
        if len(f) == 1:
            f = os.path.relpath(os.path.join(data_path, f[0]))
            str_msg += get_link_image(f, width, height, ' --- ')
            str_msg += ' | '
        else:
            str_msg += ' --- |'
    return str_msg


def dga_table(conditions, tools, data_path, width, height):
    str_msg = 'Click on figure to retrieve original PDF file\n\n'

    for c in conditions:
        files = [f for d, ds, files in os.walk(data_path) for f in files if c in f]
        str_msg += '#### Condition: ' + c.replace('_', ' ') + '\n\n'
        for t in tools:
            str_msg += '| ' + tools[t] + ' '
        str_msg += '|\n'
        for t in tools:
            str_msg += '| --- '
        str_msg += '|\n'

        str_msg += print_tools(c, tools, files, data_path, width, height)
        str_msg += '\n\n'
    return str_msg


def dga_gene_list_intersection(conditions, data_path, organism):
    str_msg = ''
    table_header = '''
    <table>
    <thead>
    <tr>
    <th>Gene</th>
    <th>logFC</th>
    <th>FDR</th>
    </tr>
    </thead>
    <tbody>
    '''
    for c in conditions:
        f = os.path.relpath(os.path.join(data_path,
                                         'condition_' + c + '_intersection.csv'))
        o = os.path.relpath(os.path.join(data_path,
                                         'condition_' + c + '_intersection_over-expressed.csv'))
        u = os.path.relpath(os.path.join(data_path,
                                         'condition_' + c + '_intersection_under-expressed.csv'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            str_msg += '\n\n### Condition: ' + c.replace('_vs_', ' vs ') + '\n\n'
            str_msg += 'Full list of genes <a href="'
            str_msg += f.replace(' ', '%20')
            str_msg += '" target="_blank">'
            str_msg += os.path.basename(f)
            str_msg += '</a>\n\n'
            str_msg += '| Genes over-expressed | Genes under-expressed |\n'
            str_msg += '| --- | --- |\n'

            over_df = pandas.read_csv(o)
            if len(over_df) > 0:
                over_df[['Gene_Id', 'Chr', 'Start_pos']] = \
                    over_df['Gene_Id'].str.split('_', n=2, expand=True)
                over_df = over_df.drop(columns=['Chr', 'Start_pos'])
            over_count = len(over_df)
            str_msg += ' | ' + str(over_count) + ' | '

            under_df = pandas.read_csv(u)
            if len(under_df) > 0:
                under_df[['Gene_Id', 'Chr', 'Start_pos']] = \
                    under_df['Gene_Id'].str.split('_', n=2, expand=True)
                under_df = under_df.drop(columns=['Chr', 'Start_pos'])
            under_count = len(under_df)
            str_msg += str(under_count) + ' |\n\n'
            if under_count > 0 or over_count > 0:
                str_msg += '<div style="display: table;width: 100%;">'
                str_msg += '<div style="display: table-row;">'
                str_msg += '<div style="display: table-cell;vertical-align:top;">\n\n'
                if len(over_df) > 0:
                    str_msg += '<h3>Top 30 Over-expressed genes</h3>'
                    str_msg += '<br>CSV file:<br><a href="'
                    str_msg += o.replace(' ', '%20')
                    str_msg += '" target="_blank">'
                    str_msg += os.path.basename(o)
                    str_msg += '</a><br>'
                    str_msg += table_header
                    for i, r in over_df.head(30).iterrows():
                        str_msg += '<tr>'
                        str_msg += '<td>'
                        str_msg += '<a href="https://www.ncbi.nlm.nih.gov/gene/?term=' \
                                   + r['Gene_Id'] + '%5BGene+Name%5D+AND+' \
                                   + organism.replace(' ', '+') \
                                   + '%5BOrganism%5D" target="_blank">' \
                                   + r['Gene_Id'] + '</a>'
                        str_msg += '</td>'
                        str_msg += '<td>' + "{:.3f}".format(r['logFC']) + '</td>'
                        str_msg += '<td>' + "{:.3e}".format(r['FDR']) + '</td>'
                        str_msg += '</tr>'
                    str_msg += '</tbody></table>'
                str_msg += '</div>'
                str_msg += '<div style="display: table-cell;vertical-align:top;">\n\n'
                if len(under_df) > 0:
                    str_msg += '<h3>Top 30 Under-expressed genes</h3>'
                    str_msg += '<br>CSV file:<br><a href="'
                    str_msg += u.replace(' ', '%20')
                    str_msg += '" target="_blank">'
                    str_msg += os.path.basename(u)
                    str_msg += '</a><br>'
                    str_msg += table_header
                    for i, r in under_df.head(30).iterrows():
                        str_msg += '<tr>'
                        str_msg += '<td>'
                        str_msg += '<a href="https://www.ncbi.nlm.nih.gov/gene/?term=' \
                                   + r['Gene_Id'] + '%5BGene+Name%5D+AND+' \
                                   + organism.replace(' ', '+') \
                                   + '%5BOrganism%5D" target="_blank">' \
                                   + r['Gene_Id'] + '</a>'
                        str_msg += '</td>'
                        str_msg += '<td>' + "{:.3f}".format(r['logFC']) + '</td>'
                        str_msg += '<td>' + "{:.3e}".format(r['FDR']) + '</td>'
                        str_msg += '</tr>'
                    str_msg += '</tbody></table>'
                str_msg += '</div>'
                str_msg += '</div>'
                str_msg += '</div>'
    return str_msg
