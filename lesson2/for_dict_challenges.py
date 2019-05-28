# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
print("\nДан список учеников, нужно посчитать количество повторений каждого имени ученика.")
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

for i in set(name['first_name'] for name in students):
  print("{}: {}".format(i, students.count({"first_name": i})))


# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
print("\nДан список учеников, нужно вывести самое часто повторяющееся имя.")
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

names_len =  {name['first_name']: students.count(name) for name in students }
print("The most favorite name: {}". format(sorted(names_len.items(), key=lambda kv: kv[1], reverse=True)[0][0]))


print("")

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
print("\nЕсть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.")
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

for school in school_students:
  name_cnt = {}
  for stud in school:
    name_cnt[stud["first_name"]] = school.count(stud)
  print("The most favorite name in class {}: {}".format(school_students.index(school)+1, (sorted(name_cnt.items(), key=lambda kv: kv[1], reverse=True)[0][0])))

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
print("\nДля каждого класса нужно вывести количество девочек и мальчиков в нём.")
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for klass in school:
  male = 0
  female = 0
  for stud in klass["students"]:
    if is_male[stud["first_name"]]:
      male += 1
    else:
      female += 1
  print("In {} are {} females and {} males".format(klass["class"], female, male))

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
print("\nПо информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.")
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school_count = {}

for klass in school:
  male = 0
  female = 0
  for stud in klass["students"]:
    if is_male[stud["first_name"]]:
      male += 1
    else:
      female +=1
  school_count[klass["class"]] = [{"males": male}, {"females": female}]

for cnt in  school_count.keys():
  if school_count[cnt][0]["males"] > school_count[cnt][1]["females"]:
    print("The most of males are in {} class".format(cnt))
  else:
    print("The most of females are in {} class".format(cnt))


