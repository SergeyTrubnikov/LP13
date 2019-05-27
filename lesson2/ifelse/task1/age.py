
AGE = abs(int(input("Enter your age: ")))

SCHOOL = 7
UNIVERSITY = 17
WORK = 22


def check_age(age: int) -> str:
    if age < SCHOOL:
        return "You are in Kindergarten :)"
    elif SCHOOL <= age < UNIVERSITY:
        return "You are at School"
    elif UNIVERSITY <= age < WORK:
        return "You are at University"
    else:
        return "You are at Work"


occupation = check_age(AGE)

print("Your occupation:\n{}".format(occupation))

