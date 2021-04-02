class Time:
    """
    Represents the time of day.
    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize the object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Returns a string representation of the time."""
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'

    # create a method called print_time
    def print_time(self):
        """Prints a string representation of the time."""
        print(f'{self.hour:02}:{self.minute:02}:{self.second:02}')

    # Exercise 1
    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    It is a helper function.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def main():
    # t1 = Time()
    # t1.hour = 21
    # t1.minute = 1
    # t1.second = 30
    t1 = Time(21, 1, 30)  # Initialization

    # t1.print_time()
    print(t1)
    print(t1.time_to_int())

    # t2 = Time()
    # t2.hour = 21
    # t2.minute = 10
    # t2.second = 0
    t2 = Time(21, 10, 0)
    t2.print_time()

    print(t2.is_after(t1))

    beginning = Time()
    beginning.print_time()


if __name__ == '__main__':
    main()