from utils import read_input


def part1(lines):
    return sum(check_line(line) for line in lines)


def part2(lines):
    return sum(any(check_line(line[:i] + line[i+1:]) for i in range(len(line))) for line in lines)


def check_line(line):
    monotone_increase = all(line[i] < line[i + 1] for i in range(len(line) - 1))
    monotone_decrease = all(line[i] > line[i + 1] for i in range(len(line) - 1))
    valid_diffs = all(1 <= abs(line[i] - line[i + 1]) <= 3 for i in range(len(line) - 1))
    return (monotone_increase or monotone_decrease) and valid_diffs


if __name__ == '__main__':
    input_data = read_input('inputs/day2.txt')
    input_data = [[int(n) for n in row.split()] for row in input_data]
    print(part1(input_data))
    print(part2(input_data))
