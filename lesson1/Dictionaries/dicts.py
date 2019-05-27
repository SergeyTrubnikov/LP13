
phones = ["iPhone", "Xiaomi", "Huawei"]


product = {
    "name" : "Xiaomi",
    "stock" : 25,
    "price" : 35500.00
}

product["recommended"] = phones
product["recommended"].append('Nokia') 


# print(product["recommended"])

print(type(product))
print(type(product["recommended"]))
