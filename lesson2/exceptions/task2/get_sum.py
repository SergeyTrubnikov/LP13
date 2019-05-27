
def get_sum(num_one, num_two):
    try:
        num_one = int(num_one)
    except ValueError:
        return "Cannot convert {} type to int".format(num_one)

    try:
        num_two = int(num_two)
    except ValueError:
        return "Cannot convert {} type to int".format(num_two)

    return num_one + num_two


print(get_sum('10', '15,'))

