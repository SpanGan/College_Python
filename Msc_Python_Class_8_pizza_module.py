def make_pizza(*toppings,size=6):
    print(f'Pizza of {size} inches with the following toppings')
    [print(topping) for topping in toppings] 