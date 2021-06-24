import os
import pandas

from pm4ngs.jupyterngsplugin.image.pngtobase64 import imagetobase64


def go_plots_table(conditions, data_path, width, height):
    str_msg = ''
    for c in conditions:
        str_msg += '\n\n### Condition: ' + c.replace('_vs_', ' vs ') + '\n\n'

        str_msg += '\n\n| Biological process | Molecular Function | Cellular Component |\n'
        str_msg += '| --- | --- | --- |\n'
        f = os.path.relpath(os.path.join(data_path, 'go_biological_process_' + c + '_intersection.png'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            str_msg += '| <a href="'
            str_msg += f.replace(' ', '%20')
            str_msg += '" target="_blank">'
            str_msg += '<img src="data:image/png;base64,' + imagetobase64(f, width, height) + '">'
            str_msg += '</a> |'
        else:
            str_msg += '| --- |'
        f = os.path.relpath(os.path.join(data_path, 'go_molecular_function_' + c + '_intersection.png'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            str_msg += ' <a href="'
            str_msg += f.replace(' ', '%20')
            str_msg += '" target="_blank">'
            str_msg += '<img src="data:image/png;base64,' + imagetobase64(f, width, height) + '">'
            str_msg += '</a> |'
        else:
            str_msg += ' --- |'
        f = os.path.relpath(os.path.join(data_path, 'go_cellular_component_' + c + '_intersection.png'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            str_msg += ' <a href="'
            str_msg += f.replace(' ', '%20')
            str_msg += '" target="_blank">'
            str_msg += '<img src="data:image/png;base64,' + imagetobase64(f, width, height) + '">'
            str_msg += '</a> |'
        else:
            str_msg += ' --- |\n'
    str_msg += '\n\n'
    return str_msg


def print_count_table(c, namespaces, data_path):
    str_msg = ''
    for n in namespaces:
        str_msg += '|' + n.replace('_', ' ') + '|'
        f = os.path.relpath(os.path.join(data_path, 'go_over_' + n + '_' + c + '_intersection.csv'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            df = pandas.read_csv(f)
            str_msg += ' {0} |'.format(len(df))
        else:
            str_msg += '--- |'
        f = os.path.relpath(os.path.join(data_path, 'go_under_' + n + '_' + c + '_intersection.csv'))
        if os.path.exists(f) and os.path.getsize(f) != 0:
            df = pandas.read_csv(f)
            str_msg += ' {0} |'.format(len(df))
        else:
            str_msg += '--- |'
        str_msg += '\n'
    str_msg += '\n\n'
    return str_msg


def print_table_cell(filename, title):
    str_msg = ''
    table_header = '''
    <table>
    <thead>
    <tr>
    <th>GO term</th>
    <th>Name</th>
    <th>FDR</th>
    </tr>
    </thead>
    <tbody>
    '''
    if os.path.exists(filename) and os.path.getsize(filename) != 0:
        df = pandas.read_csv(filename)
        if len(df) > 0:
            str_msg += '<div style="display: table-cell;vertical-align:top;">'
            str_msg += '<h4>'
            str_msg += title
            str_msg += '</h4>'
            str_msg += '<br>CSV file:<br><a href="'
            str_msg += filename.replace(' ', '%20')
            str_msg += '" target="_blank">'
            str_msg += 'raw file'
            str_msg += '</a><br>'
            str_msg += table_header
            for i, r in df.head(30).iterrows():
                str_msg += '<tr>'
                str_msg += '<td>'
                str_msg += '<a href="https://www.ebi.ac.uk/QuickGO/term/' + r['term']
                str_msg += '" target="_blank">'
                str_msg += r['term'] + '</a>'
                str_msg += '</td>'
                str_msg += '<td>' + r['name'][:40] + '</td>'
                str_msg += '<td>' + "{:.3e}".format(r['q']) + '</td>'
                str_msg += '</tr>'
            str_msg += '</tbody></table>'
            str_msg += '</div>'
    return str_msg


def go_html_table(conditions, data_path):
    str_msg = ''
    for c in conditions:
        str_msg += '\n\n### Condition: ' + c.replace('_vs_', ' vs ') + '\n\n'
        str_msg += '#### GO terms per name space \n\n'
        namespaces = [f.replace('go_over_', '').replace('_' + c + '_intersection.csv', '')
                      for d, ds, files in
                      os.walk(data_path) for f in files
                      if f.startswith('go_over_') and f.endswith('.csv') and c in f]
        str_msg += '| Name space | Over | Under |\n'
        str_msg += '| --- | --- | --- |\n'
        str_msg += print_count_table(c, namespaces, data_path)
        str_msg += '\n\n'

        for n in namespaces:
            str_msg += '<div><h3>Top 30 GO terms for ' + n.replace('_', ' ') + '</h3>'
            str_msg += '<div style="display: table;width: 100%;">'
            str_msg += '<div style="display: table-row;">'
            f = os.path.relpath(os.path.join(data_path, 'go_over_' + n + '_' + c + '_intersection.csv'))
            str_msg += print_table_cell(f, 'Over-expressed')
            f = os.path.relpath(os.path.join(data_path, 'go_under_' + n + '_' + c + '_intersection.csv'))
            str_msg += print_table_cell(f, 'Under-expressed')
            str_msg += '</div></div></div>'
        str_msg += '\n'
    return str_msg
