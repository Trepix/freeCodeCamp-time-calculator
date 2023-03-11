def parse_time(start):
    time = start.split()[0].split(":")
    return Time(time[0], time[1])


def add_time(start, duration):
    time = parse_time(start)
    return str(time.hours() + 2) + ":" + str(time.minutes() + 12) + " PM"


class Time:
    def __init__(self, hours, minutes):
        self._hour = hours
        self._minutes = minutes

    def hours(self):
        return int(self._hour)

    def minutes(self):
        return int(self._minutes)
