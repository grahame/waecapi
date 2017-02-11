import argparse
from .api import election_candidates


def command_download(args):
    election_candidates('sg2017')


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
