
def str_compare(one, two):
    if type(one) != str or type(two) != str:
        return 0
    elif one == two:
        return 1
    elif len(one) > len(two) and two == "learn":
        return [2, 3]
    elif len(one) > len(two):
        return 2
    elif two == "learn":
        return 3
    else:
        return "The strings are just different: {} and {}".format(one, two)


print(str_compare(10, "learn"))
print(str_compare("learn", "learn"))
print(str_compare("learnlearn", "learn"))
print(str_compare("string", ""))
print(str_compare("strin", "learn"))
print(str_compare("string", "longstring"))


