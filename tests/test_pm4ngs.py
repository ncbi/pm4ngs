import requests
from pm4ngs.main import PIPELINES


def test_main_rnase_name():
    assert PIPELINES[1]['name'] == 'RNA-Seq'


def test_main_rnase_url():
    url = PIPELINES[1]['url']
    request = requests.get(url)
    assert request.status_code == 200
