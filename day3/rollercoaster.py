print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height < 120:
    print(
        f"Sorry, you are not tall enough to ride this rollercoaster."
        f"\nCome back later when you are taller!"
        f"\nHave a good day!")
elif height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        print(
            "Sorry, you are not old enough to ride this rollercoaster,"
            "you need to be 12 years old or older to ride this rollercoaster."
        )
    elif age >= 12 and height >= 120:
        print("Enjoy the ride!"
              "\nHave a good day!")
