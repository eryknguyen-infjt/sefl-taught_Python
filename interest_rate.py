def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    data = [list(map(int, line.split())) for line in lines]
    return data


def calculate_amount(c, t, A, k, h, m):
    if c == 0:
        if t <= m:
            return round(A * (1 + k / 100) ** t, 1)
        else:
            return round(A * (1 + k / 100) ** m + (A * (1 + h / 100) ** (t - m)), 1)
    else:
        if t <= c:
            return round(A * (1 + k / 100) ** t, 1)
        else:
            return round(A * (1 + k / 100) ** c + (A * (1 + h / 100) ** (t - c)), 1)


def write_output(file_name, amounts):
    with open(file_name, 'w') as file:
        for amount in amounts:
            file.write(f'{amount}\n')


def main():
    input_data = read_input('general.inp')
    output_data = [calculate_amount(*data) for data in input_data]
    write_output('general.out', output_data)


if __name__ == '__main__':
    main()
