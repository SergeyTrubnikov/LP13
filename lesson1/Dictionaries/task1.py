
dict1 = {
    "city" : "Moscow",
    "temperature" : "20"
}

print(dict1["city"])

dict1["temperature"] = str(int(dict1["temperature"]) - 5)
print(dict1)

print(dict1.get('country'))
print(dict1.get('country', "Russia"))
dict1["date"] = "27.05.2019"
print(dict1)

print(len(dict1))