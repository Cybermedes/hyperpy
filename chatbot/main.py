def greet(bot_name: str, birth_year: int) -> None:
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name() -> None:
    print("Please, remind me your name.")
    name: str = input()
    print(f"What a great name you have, {name}!")


def guess_age() -> None:
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age: int = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count() -> None:
    print("Now I will prove to you that I can count to any number you want.")

    num = int(input())
    curr: int = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test() -> None:
    print("Let's test your programming knowledge.")
    print("""What of these programming languages is a compiled one?
1. Java
2. Python
3. Go
4. Javascript""")

    while True:
        answer: int = int(input())
        if answer == 3:
            break
        print("Please, try again.")


def end() -> None:
    print("Congratulations, have a nice day!")


def main() -> None:
    greet("Zoox", 2024)
    remind_name()
    guess_age()
    count()
    test()
    end()


if __name__ == "__main__":
    main()
