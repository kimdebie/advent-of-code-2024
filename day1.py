from collections import Counter

from utils import read_input


def part1(firsts, seconds):
    firsts.sort()
    seconds.sort()
    return sum(abs(f - s) for f, s in zip(firsts, seconds))


def part2(firsts, seconds):
    second_counts = Counter(seconds)
    return sum(n * second_counts[n] for n in firsts)


def split_firsts_seconds(input):
    numbers = [[int(n) for n in row.split()] for row in input]
    firsts, seconds = [list(l) for l in zip(*numbers)]
    return firsts, seconds


if __name__ == '__main__':
    input = read_input('inputs/day1.txt')
    firsts, seconds = split_firsts_seconds(input)
    print(part1(firsts, seconds))
    print(part2(firsts, seconds))

