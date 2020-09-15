import xmltodict
import collections
import pandas
from Bio import Entrez

from time import sleep
from urllib.error import HTTPError


def runs_from_bioproject_id(bioproject_id, email, eutils_key=None):
    Entrez.email = email
    if eutils_key:
        Entrez.api_key = eutils_key
    handle = Entrez.esearch(db="sra", term=bioproject_id, retmax=50)
    sra_id = Entrez.read(handle)
    handle.close()
    tuples = []
    i = len(sra_id['IdList']) - 1
    while i >= 0:
        try:
            handle = Entrez.efetch(db="sra",
                                   id=sra_id['IdList'][i],
                                   rettype="full", retmode="full")
            sra = xmltodict.parse(handle.read())
            handle.close()
            sra_data = sra['EXPERIMENT_PACKAGE_SET']['EXPERIMENT_PACKAGE']
            alias = '' if 'SAMPLE' not in sra_data else sra_data['SAMPLE']['@alias']
            accession = '' if 'SAMPLE' not in sra_data else sra_data['SAMPLE']['@accession']
            if type(sra_data['RUN_SET']['RUN']) is list:
                for run in sra_data['RUN_SET']['RUN']:
                    f = run['@accession']
                    tuples.append([alias, accession, f])
            elif type(sra_data['RUN_SET']['RUN']) is collections.OrderedDict:
                f = sra_data['RUN_SET']['RUN']['@accession']
                tuples.append([alias, accession, f])
            i -= 1
        except HTTPError as err:
            if err.code == 429:
                print('SRA metadata downloaded for %d/%d. '
                      'Max request reached. Retry-After: %s sec' %
                      (len(sra_id['IdList']) - i,
                       len(sra_id['IdList']),
                       err.headers['Retry-After']))
                sleep(int(err.headers['Retry-After']))
                continue

    return pandas.DataFrame(tuples, columns=['ALIAS', 'ACCESSION', 'RUN'])
