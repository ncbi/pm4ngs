import os
import pickle
import shutil
import tarfile
import tempfile

import networkx as nx
import pandas
import requests


def parse_nodes_file(node_file, taxid):
    with open(node_file, 'r') as fin:
        for line in fin:
            f = line.strip().split('\t|\t')
            node = {}
            node['id'] = f[0]
            node['name'] = taxid[f[0]]['scientific name']
            edge = ()
            if f[1] != node['id']:
                edge = (f[1], node['id'])
            yield (f[0], node), edge


def parse_tax_name_file(name_file):
    tax_id = {}
    with open(name_file, 'r') as fin:
        for line in fin:
            line = line.strip()
            f = line.split('\t|\t')
            if f[0] not in tax_id:
                tax_id[f[0]] = {}
            tax_id[f[0]][f[3].replace('\t|', '').strip()] = f[1]
    return tax_id


class Taxonomy:

    def __init__(self, *args, **kwargs):
        name_file = kwargs.get('name_file', None)
        node_file = kwargs.get('node_file', None)
        tax_pickle_file = kwargs.get('tax_pickle_file', None)
        group_pickle_file = kwargs.get('group_pickle_file', None)
        self.taxonomy_groups = kwargs.get('taxonomy_groups', {
            'bacteria': {'taxid': '2', 'nodes': set(), 'sequences': set(), 'size': 0},
            'archaea': {'taxid': '2157', 'nodes': set(), 'sequences': set(), 'size': 0},
            'viridiplantae': {'taxid': '33090', 'nodes': set(), 'sequences': set(), 'size': 0},
            'fungi': {'taxid': '4751', 'nodes': set(), 'sequences': set(), 'size': 0},
            'arthropoda': {'taxid': '6656', 'nodes': set(), 'sequences': set(), 'size': 0},
            'neoteleostei': {'taxid': '123365', 'nodes': set(), 'sequences': set(), 'size': 0},
            'actinopterygii': {'taxid': '7898', 'nodes': set(), 'sequences': set(), 'size': 0},
            'glires': {'taxid': '314147', 'nodes': set(), 'sequences': set(), 'size': 0},
            'primates': {'taxid': '9443', 'nodes': set(), 'sequences': set(), 'size': 0},
            'carnivora': {'taxid': '33554', 'nodes': set(), 'sequences': set(), 'size': 0},
            'artiodactyla': {'taxid': '91561', 'nodes': set(), 'sequences': set(), 'size': 0},
            'amphibia': {'taxid': '8292', 'nodes': set(), 'sequences': set(), 'size': 0},
            'sauropsida': {'taxid': '8457', 'nodes': set(), 'sequences': set(), 'size': 0},
            'sarcopterygii': {'taxid': '8287', 'nodes': set(), 'sequences': set(), 'size': 0},
            'chordata': {'taxid': '7711', 'nodes': set(), 'sequences': set(), 'size': 0},
            'eukaryota': {'taxid': '2759', 'nodes': set(), 'sequences': set(), 'size': 0},
            'viruses': {'taxid': '10239', 'nodes': set(), 'sequences': set(), 'size': 0},
        })
        self.tax = nx.DiGraph()
        if name_file and node_file:
            self.create_taxonomy_graph(name_file, node_file)
            self.create_taxonomy_groups()
        elif tax_pickle_file:
            self.tax = pickle.load(open(tax_pickle_file, "rb"))
            print('{} taxonomies loaded'.format(len(self.tax.nodes())))
            self.taxonomy_groups = pickle.load(open(group_pickle_file, "rb"))
            for k in self.taxonomy_groups:
                print('{} Node: {} Sequences: {}'.format(
                    k, len(self.taxonomy_groups[k]['nodes']),
                    len(self.taxonomy_groups[k]['sequences'])
                ))
        else:
            self.create_taxonomy_from_data()
            self.create_taxonomy_groups()

    def create_taxonomy_from_data(self):
        print('Downloading NCBI Taxonomy database')
        dirpath = tempfile.mkdtemp()
        url = 'https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz'
        response = requests.get(url, stream=True)
        file = tarfile.open(fileobj=response.raw, mode="r|gz")
        file.extractall(path=dirpath)
        self.create_taxonomy_graph(os.path.join(dirpath, 'names.dmp'),
                                   os.path.join(dirpath, 'nodes.dmp'))

        shutil.rmtree(dirpath)

    def successors(self, g):
        """
        Extract ancestors nodes from an starting node
        :param g: starting node name
        :param O: Graph
        :return: a set with node names
        """
        result = {g}
        for o in self.tax.successors(g):
            result.update(self.successors(o))
        return result

    def find_node(self, id):
        nodes = [y for x, y in self.tax.nodes(data=True) if y['id'] == id]
        if nodes:
            a = ""
            for i in nx.shortest_path(self.tax, source="1", target=id)[2:]:
                ns = [y for x, y in self.tax.nodes(data=True) if y['id'] == i]
                if ns:
                    if a:
                        a += "; "
                    a += ns[0]['name']
            return nodes[0], a
        return None, None

    def find_node_by_name(self, name):
        for n in self.tax.nodes(data=True):
            if n[1]['name'].casefold() == name.casefold():
                return n
        return None

    def get_node_lineage(self, node):
        a = ""
        for i in nx.shortest_path(self.tax, source="1", target=node[0])[2:]:
            ns = [y for x, y in self.tax.nodes(data=True) if y['id'] == i]
            if ns:
                if a:
                    a += "; "
                a += ns[0]['name']
        return a

    def get_lineage_by_name(self, name):
        n = self.find_node_by_name(name)
        return self.get_node_lineage(n)

    def create_taxonomy_graph(self, name_file, node_file):
        tax_id = parse_tax_name_file(name_file)
        print('Taxonomies: {}'.format(len(tax_id)))
        entries = parse_nodes_file(node_file, tax_id)
        nodes, edges = zip(*entries)
        print('{} nodes created'.format(len(nodes)))
        self.tax.add_nodes_from(nodes)
        for e in edges:
            if e:
                self.tax.add_edge(*e)

    def get_successors(self, taxid):
        return set([int(i) for i in self.successors(taxid)])

    def get_taxonomy_group_nodes(self, taxid, to_exclude):
        self.taxonomy_groups[taxid]['nodes'] = \
            self.get_successors(self.taxonomy_groups[taxid]['taxid'])
        self.taxonomy_groups[taxid]['nodes'] = \
            list(set(self.taxonomy_groups[taxid]['nodes']) - to_exclude)
        print('{} with {} taxa'.format(taxid, len(self.taxonomy_groups[taxid]['nodes'])))

    def add_sequences_sizefrom_gtax_idx(self, taxonomy_group):
        if os.path.exists('{}.idx'.format(taxonomy_group)):
            df = pandas.read_csv('{}.idx'.format(taxonomy_group), sep='\t', header=None)
            print('{} sequences loaded from the index'.format(len(df)))
            seq = {}
            for g in df.groupby(2):
                seq[str(g[0])] = {'sequences': set(g[1][0].unique()), 'size': g[1][3].sum()}
            nx.set_node_attributes(self.tax, seq)

    def create_taxonomy_groups(self):
        inserted = set()
        nodes = self.tax.nodes(data=True)
        for k in self.taxonomy_groups:
            self.taxonomy_groups[k]['nodes'] = self.get_successors(self.taxonomy_groups[k]['taxid']).difference(
                inserted)
            inserted.update(self.taxonomy_groups[k]['nodes'])
            self.add_sequences_sizefrom_gtax_idx(k)
            for node_id in self.taxonomy_groups[k]['nodes']:
                node_id = str(node_id)
                if 'size' in nodes[node_id]:
                    self.taxonomy_groups[k]['sequences'].update(nodes[node_id]['sequences'])
                    self.taxonomy_groups[k]['size'] += nodes[node_id]['size']

    def create_pickle(self, tax_pickle_file, group_pickle_file):
        print('Printing tax graph pickle file')
        pickle.dump(self.tax, open(tax_pickle_file, "wb"))
        print('Printing tax group pickle file')
        pickle.dump(self.taxonomy_groups, open(group_pickle_file, "wb"))

    def print_size(self, node_name, deep=1, step=1, min_size=10.0, min_size_child=50.0):
        nodes = self.tax.nodes(data=True)
        node = self.find_node_by_name(node_name)
        size = 0
        taxa = 0
        for node_id in self.successors(node[1]['id']):
            if 'sequences' in nodes[node_id]:
                taxa += 1
                size += nodes[node_id]['size']
        size = size / 1e+9
        if size >= min_size:
            print('{}{} {} => {:.2f} GB'.format('   ' * step, node_name, node[1]['id'], size))
        step += 1
        if step < deep and size >= min_size_child:
            for t in self.tax.successors(node[1]['id']):
                if t != node[1]['id']:
                    self.print_size(self.find_node(t)[0]['name'], deep, step, min_size, min_size_child)

    def resume(self):
        data = []
        nodes = self.tax.nodes(data=True)
        for k in self.taxonomy_groups:
            taxas = 0
            for n in self.taxonomy_groups[k]['nodes']:
                if 'sequences' in nodes[str(n)]:
                    taxas += 1
            data.append([k, len(self.taxonomy_groups[k]['nodes']),
                         taxas,
                         len(self.taxonomy_groups[k]['sequences']),
                         round(self.taxonomy_groups[k]['size'] / 1e+9, 2)])
        return pandas.DataFrame(data, columns=['Taxonomy', 'Taxas', 'Taxas with sequences', 'Sequences', 'Size (GB)'])

