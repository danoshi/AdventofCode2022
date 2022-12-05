"""Advent of Code Puzzle - day 3"""

import string
from pathlib import Path

input_file = Path(__file__).parent.parent / "inputs" / "03wzhkdi.txt"


def alphabet() -> string:
    alphabet_lowercase = string.ascii_lowercase
    alphabet_uppercase = string.ascii_uppercase
    alphabet = '0' + alphabet_lowercase + alphabet_uppercase
    return alphabet


def readfile(file):
    rucksack = open(file, "r").readlines()
    items = [elf.replace('\n', '') for elf in rucksack]
    return items


def item_split() -> list:
    items = readfile(input_file)
    letters = []
    for item in items:
        first_item = item[:len(item) // 2]
        second_item = item[len(item) // 2:]
        letters.append(''.join(set(first_item).intersection(second_item)))
    return letters


def position() -> list:
    alphabet_list = item_split()
    alp = alphabet()
    letter_position = []
    for letter in alphabet_list:
        if letter in alp:
            letter_position.append(alp.index(letter))
    return letter_position


def position_2() -> list:
    alphabet_list = readfile(input_file)
    groups = []
    for group in range(0, len(alphabet_list), 3):
        current_group = [set(el) for el in alphabet_list[group:group + 3]]
        groups.append(list(set.intersection(*current_group))[0])
    return groups


def value_2() -> list:
    alphabet_list = position_2()
    alp = alphabet()
    letter_position = []
    for letter in alphabet_list:
        if letter in alp:
            letter_position.append(alp.index(letter))
    return letter_position


def calc(letter: list) -> int:
    erg = 0
    for p in letter:
        erg += p
    return erg


def puzzle_1() -> int:
    alp = position()
    return calc(alp)


def puzzle_2() -> int:
    alp = value_2()
    return calc(alp)
