import argparse
import sys
import csv

from .api import election_candidates


def command_download(args):
    electorates = []
    candidates = []
    for electorate, candidate in election_candidates('sg2017'):
        electorates.append(electorate)
        candidates.append(candidate)
    fields = []
    for candidate in candidates:
        for k in candidate:
            if k not in fields:
                fields.append(k)

    w = csv.writer(sys.stdout)
    w.writerow(['ELECTORATE_TYPE', 'ELECTORATE_NAME'] + fields)
    for electorate, candidate in zip(electorates, candidates):
        row = [electorate['ElelctorateType'], electorate['ElectorateName']] + [candidate.get(t, '') for t in fields]
        w.writerow(row)


def main():
    commands = {
        'candidates': command_download,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        help='action to take',
        nargs='?',
        default='candidates',
        choices=commands.keys())
    args = parser.parse_args()
    commands[args.command](args)
