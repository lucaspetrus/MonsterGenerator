class Printable:

    def __str__(self):
        return '\n'.join(f"{k.title()}: {v}" for k, v in self.__dict__.items())


def mean(arr) -> float:
    """ Calculates the average value of the input Iterable """
    return sum(arr) / len(arr)
