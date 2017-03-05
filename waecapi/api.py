import requests
import sys

API_BASE = 'https://api.elections.wa.gov.au/sgElections/'


def sg_elections(election_name):
    url = API_BASE
    if election_name:
        url = url + election_name
    sys.stderr.write(url + '\n')
    sys.stderr.flush()
    return requests.get(url).json()


def region_url(election_name, code):
    return API_BASE + election_name + '/region/' + code


def district_url(election_name, code):
    return API_BASE + election_name + '/' + code


def get_candidates(url_base):
    url = url_base + '/candidates'
    sys.stderr.write(url + '\n')
    sys.stderr.flush()
    json = requests.get(url).json()
    if 'districtCandidates' in json:
        return json['districtCandidates']
    if 'regionCandidates' in json:
        return json['regionCandidates']


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
        for candidate in candidates:
            yield electorate, candidate
