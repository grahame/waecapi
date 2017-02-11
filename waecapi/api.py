import requests
from pprint import pprint

API_BASE = 'https://api.elections.wa.gov.au/sgElections/'


def sg_elections(election_name):
    url = API_BASE
    if election_name:
        url = url + election_name
    return requests.get(url).json()


def region_url(election_name, code):
    return API_BASE + election_name + '/region/' + code


def district_url(election_name, code):
    return API_BASE + election_name + '/' + code


def get_candidates(url_base):
    url = url_base + '/candidates'
    pprint(url)
    return requests.get(url).json()


def election_candidates(election_name):
    for electorate in sg_elections(election_name)['electorates']:
        typ, code = electorate['ElelctorateType'], electorate['ElectorateCode']
        url = None
        if typ == 'Region':
            url = region_url(election_name, code)
        elif typ == 'District':
            url = district_url(election_name, code)
        if url is None:
            continue
        candidates = get_candidates(url)
        pprint(candidates)