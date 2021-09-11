"這個冰淇淋所加配料如下"
def make_icecream(*toppings):
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ",topping)
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')