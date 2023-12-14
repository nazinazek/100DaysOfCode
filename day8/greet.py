def greet():
    print(f"Hello")
    print(f"How are you?")
    print(f"Isn't the weather nice today?")


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print(f"Isn't the weather nice today {name}?")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with("Naz", "Almaty")