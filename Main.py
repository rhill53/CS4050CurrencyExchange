"""
Robb Hill
CS4050
Program 5
"""
import sys
import subprocess
import os
from itertools import permutations

graph = []
currencies = []
rates = {}


def create_graph():
    for v1, v2, edge in graph:
        if (v1, v2) not in rates:
            rates[(v1, v2)] = float(edge)
        if (v2, v1) not in rates:
            rates[(v2, v1)] = 1/(float(edge))


def exchanges(vertices):
    first, *remaining = vertices
    for vertex in range(1, len(remaining) + 1):
        for perm in permutations(remaining, vertex):
            yield [first] + list(perm) + [first]


def add_edge(v1, v2, edge):
    graph.append([v1, v2, edge])


def read_file(file_name):
    with open(file_name, 'r') as lines:
        for line in lines:
            try:
                parts = line.strip('\\t')
                v1, v2, edge = parts.split()
                if v1 not in currencies:
                    currencies.append(v1)
                if v2 not in currencies:
                    currencies.append(v2)
                add_edge(v1, v2, edge)
            except ValueError:
                pass
            except EOFError:
                break
            except None:
                pass


def step_3_profit():
    for path in exchanges(currencies):
        edges = list(zip(path[:-1], path[1:]))
        cost = 1.0
        for edge in edges:
            cost *= rates[edge]
        if cost > 1.0:
            amount = round(1000*cost, 2)
            print(f'{amount:.2f} result if the path {path} is chosen')


def main():
    try:
        read_file(sys.argv[1])
    except IndexError:
        file_path = str(input('Enter path to file for exchange rates: \n'))
        read_file(file_path)

    create_graph()
    step_3_profit()


if __name__ == '__main__':
    try:
        command = 'start cmd python3 "' + sys.argv[1] + '"'
        subprocess.run(command, shell=True)
    except IndexError:
        pass
    main()
    os.system('PAUSE')
    print('Closing...')
