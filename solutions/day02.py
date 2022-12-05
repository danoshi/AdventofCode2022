"""Advent of Code Puzzle - day 2"""

from pathlib import Path

input_file = Path(__file__).parent.parent / "inputs" / "02wzhkdi.txt"


def readfile(file):
    game = open(file, "r").readlines()
    r_p_z = [elf.replace('\n', '') for elf in game]
    return r_p_z


def rules_puzzl1(moves: list):
    erg = 0
    for points in moves:
        if points.split()[0] == 'A' and points.split()[1] == 'X':
            erg += 4
        if points.split()[0] == 'A' and points.split()[1] == 'Y':
            erg += 8
        if points.split()[0] == 'A' and points.split()[1] == 'Z':
            erg += 3
        if points.split()[0] == 'B' and points.split()[1] == 'X':
            erg += 1
        if points.split()[0] == 'B' and points.split()[1] == 'Y':
            erg += 5
        if points.split()[0] == 'B' and points.split()[1] == 'Z':
            erg += 9
        if points.split()[0] == 'C' and points.split()[1] == 'X':
            erg += 7
        if points.split()[0] == 'C' and points.split()[1] == 'Y':
            erg += 2
        if points.split()[0] == 'C' and points.split()[1] == 'Z':
            erg += 6
    return erg


def rules_puzzl2(moves: list):
    erg = 0
    for points in moves:
        if points.split()[0] == 'A' and points.split()[1] == 'X':
            erg += 3
        if points.split()[0] == 'A' and points.split()[1] == 'Y':
            erg += 4
        if points.split()[0] == 'A' and points.split()[1] == 'Z':
            erg += 8
        if points.split()[0] == 'B' and points.split()[1] == 'X':
            erg += 1
        if points.split()[0] == 'B' and points.split()[1] == 'Y':
            erg += 5
        if points.split()[0] == 'B' and points.split()[1] == 'Z':
            erg += 9
        if points.split()[0] == 'C' and points.split()[1] == 'X':
            erg += 2
        if points.split()[0] == 'C' and points.split()[1] == 'Y':
            erg += 6
        if points.split()[0] == 'C' and points.split()[1] == 'Z':
            erg += 7
    return erg


def puzzle_1():
    strategy = readfile(input_file)
    points = rules_puzzl1(strategy)
    return points


def puzzle_2():
    strategy = readfile(input_file)
    points = rules_puzzl2(strategy)
    return points
