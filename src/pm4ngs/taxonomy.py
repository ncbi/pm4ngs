import os
import pickle
import requests
import tarfile
import tempfile
import shutil

import networkx as nx


class Taxonomy:

    def __init__(self, *args, **kwargs):
        name_file = kwargs.get('name_file', None)
        node_file = kwargs.get('node_file', None)
        tax_pickle_file = kwargs.get('tax_pickle_file', None)
        group_pickle_file = kwargs.get('group_pickle_file', None)
        self.taxonomy_groups = kwargs.get('taxonomy_groups', {
            'bacteria': {'taxid': '2', 'nodes': set(), 'sequences': set()},
            'archaea': {'taxid': '2157', 'nodes': set(), 'sequences': set()},
            'viridiplantae': {'taxid': '33090', 'nodes': set(), 'sequences': set()},
            'fungi': {'taxid': '4751', 'nodes': set(), 'sequences': set()},
            'arthropoda': {'taxid': '6656', 'nodes': set(), 'sequences': set()},
            'chordata': {'taxid': '7711', 'nodes': set(), 'sequences': set()},
            'metazoa': {'taxid': '33208', 'nodes': set(), 'sequences': set()},
            'eukaryota': {'taxid': '2759', 'nodes': set(), 'sequences': set()},
            'viruses': {'taxid': '10239', 'nodes': set(), 'sequences': set()},
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

    def parse_nodes_file(self, node_file, taxid):
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

    def parse_tax_name_file(self, name_file):
        tax_id = {}
        with open(name_file, 'r') as fin:
            for line in fin:
                line = line.strip()
                f = line.split('\t|\t')
                if f[0] not in tax_id:
                    tax_id[f[0]] = {}
                tax_id[f[0]][f[3].replace('\t|', '').strip()] = f[1]
        return tax_id

    def create_taxonomy_graph(self, name_file, node_file):
        tax_id = self.parse_tax_name_file(name_file)
        print('Taxonomies: {}'.format(len(tax_id)))
        entries = self.parse_nodes_file(node_file, tax_id)
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

    def create_taxonomy_groups(self):
        for k in self.taxonomy_groups:
            if k != 'metazoa' and k != 'eukaryota':
                self.taxonomy_groups[k]['nodes'] = \
                    self.get_successors(self.taxonomy_groups[k]['taxid'])
                print('{} with {} taxa'.format(k, len(self.taxonomy_groups[k]['nodes'])))

        to_exclude = set(list(self.taxonomy_groups['arthropoda']['nodes'])
                         + list(self.taxonomy_groups['chordata']['nodes']))
        self.get_taxonomy_group_nodes('metazoa', to_exclude)
        to_exclude = set(
            list(to_exclude) +
            list(self.taxonomy_groups['viridiplantae']['nodes']) +
            list(self.taxonomy_groups['fungi']['nodes']) +
            list(self.taxonomy_groups['metazoa']['nodes']))
        self.get_taxonomy_group_nodes('eukaryota', to_exclude)

    def create_pickle(self, tax_pickle_file, group_pickle_file):
        print('Printing tax graph pickle file')
        pickle.dump(self.tax, open(tax_pickle_file, "wb"))
        print('Printing tax group pickle file')
        pickle.dump(self.taxonomy_groups, open(group_pickle_file, "wb"))


