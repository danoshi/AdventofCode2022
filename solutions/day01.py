from pathlib import Path

input_file = Path(__file__).parent.parent / "inputs" / "01wzhkdi.txt"


def readfile(file):
    calories = open(file, "r").readlines()
    calc = [sum(map(int, elf.split())) for elf in calories]
    return calc


def calculated_calc():
    file1 = readfile(input_file)
    max_elves = []
    total = 0
    for calc in file1:
        total += calc
        if calc == 0:
            max_elves.append(total)
            total = 0
    return max_elves


def puzzel_1():
    return max(calculated_calc())


def puzzel_2():
    calc_list = sorted(calculated_calc())
    return sum(calc_list[-3:])
