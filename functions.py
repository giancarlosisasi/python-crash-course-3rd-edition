def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


def build_user(firstname, lastname, **user_info):
    user_info[firstname] = firstname
    user_info[lastname] = lastname

    return user_info


user = build_user(firstname="Giancarlos", lastname="Isasi", email="gian@gmail.com")
print(f"User is: {user}")
