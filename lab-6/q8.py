class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return (self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds)


# Example
t1 = Time(10, 30, 15)
t2 = Time(10, 30, 15)
t3 = Time(9, 45, 20)

print(t1 == t2)  # True
print(t1 == t3)  # False
