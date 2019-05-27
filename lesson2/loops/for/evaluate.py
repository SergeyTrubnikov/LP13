
school_data = [
    {"school_class": "4a", "scores": [3,4,4,5,2]},
    {"school_class": "5b", "scores": [5,4,5,4,3]},
    {"school_class": "4b", "scores": [3,2,4,5,2]},
    {"school_class": "5c", "scores": [5,4,3,4,4]}
]

def avg_classes(school_data: list):
    for school in school_data:
        print("The average score for class {} is {}".format(school["school_class"], sum(school["scores"]) / len(school["scores"])))

def avg_school(school_data):
    school_average = []
    for school in school_data:
        school_average.append(sum(school["scores"]) / len(school["scores"]))
    print("The average for school is {}".format(sum(school_average) / len(school_average)))

avg_classes(school_data)
avg_school(school_data)


# def avg_school(avg_classes)