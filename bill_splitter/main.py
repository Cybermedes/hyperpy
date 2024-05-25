from sys import exit


def invite_friends() -> None:
    names: list[str] = []
    print("Enter the number of friends joining (including you):")
    number_people: int = int(input())

    if number_people <= 0:
        print("no one is joining for the party")
        exit(0)

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_people):
        names.append(input())

    friends: dict[str, float] = dict.fromkeys(names, 0.0)
    print(friends)


if __name__ == '__main__':
    invite_friends()
