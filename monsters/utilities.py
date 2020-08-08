class Printable:

    def __str__(self):
        return '\n'.join(f"{k.title()}: {v}" for k, v in self.__dict__.items())
