
def get_sum(one, two, delimeter = '&'):
    return delimeter.join([str(one), str(two)]).upper()

two_words_sum = get_sum('Learn','Python')
print(two_words_sum)