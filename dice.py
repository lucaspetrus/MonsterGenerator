from Pyewacket import randint


def dice(rolls: int, sides: int) -> int:
    return sum(randint(1, sides) for _ in range(rolls))


if __name__ == '__main__':
    print(dice(1, 10))
