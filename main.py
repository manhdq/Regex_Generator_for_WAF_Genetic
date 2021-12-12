import os
import base64
import random
import string
import argparse

from utils import colors
from src.parser import parser, preprocessor
from src.generator import generator


def get_data(file):
    if file == '':
        return []

    with open(file, 'r') as f:
        lines = f.readlines()

    lines = [line.rstrip() for line in lines if len(line) > 3]
    return list(set(lines))


def main(args):
    target = get_data(args.data_file)
    positive = get_data(args.positive_file)
    negative = get_data(args.negative_file)

    for line in negative:
        if line in target:
            target.remove(line)
        if line in positive:
            positive.remove(line)
    
    result = generator(target, args.population, args.generation, args.match,
                    positive=positive, negative=negative)
    
    print('\n')
    print(colors.fg.blue + 'Best regex:')
    for fit, regex in  sorted( set(result),key=lambda x : -x[0] )[:20]:
        print(colors.fg.lightblue + f'{fit}\t\t{regex}')


if __name__ == '__main__':
    Aparser = argparse.ArgumentParser()
    Aparser.add_argument('--data-file', required=True, type=str, help='data file containing uri info')
    Aparser.add_argument('--positive-file', default='', type=str, help='positive file that must be accepted')
    Aparser.add_argument('--negative-file', default='', type=str, help='negative file that must be denied')
    Aparser.add_argument('--population', default=100, type=int, help='number of phenotype candidates for genetic alg')
    Aparser.add_argument('--generation', default=20, type=int, help='number of generation to update for genetic alg')
    Aparser.add_argument('--match', default=None, type=int, help='number of uri info selected')

    args = Aparser.parse_args()

    main(args)