def parse_time(start):
    time = start.split()[0].split(":")
    return Time(time[0], time[1])


def parse_duration(duration):
    time = duration.split(":")
    return Time(time[0], time[1])


def add_time(start, duration):
    clock = parse_time(start)
    duration = parse_duration(duration)
    return str(clock.hours() + duration.hours()) + ":" + str(clock.minutes() + duration.minutes()) + " PM"


class Time:
    def __init__(self, hours, minutes):
        self._hour = hours
        self._minutes = minutes

    def hours(self):
        return int(self._hour)

    def minutes(self):
        return int(self._minutes)