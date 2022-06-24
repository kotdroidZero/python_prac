# defining new classes

class Apple:
    pass  # when you have nothing to write inside the body


class Apple:
    color=""
    flavor=""

jonaGold = Apple()
jonaGold.color = "Red"
jonaGold.flavor = "Sweet"

print(jonaGold.color)
print(jonaGold.flavor.upper())

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"

print(golden.color)
print(golden.flavor.upper())


