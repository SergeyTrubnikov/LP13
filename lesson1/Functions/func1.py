
def discounted(price, discount):
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

print(discounted(65000, 40))

