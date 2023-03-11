def parse_time(start):
    time = start.split()[0].split(":")
    return Time(time[0], time[1])


def parse_duration(duration):
    time = duration.split(":")
    return Time(time[0], time[1])


def add_time(start, duration):
    clock = parse_time(start)
    duration = parse_duration(duration)
    result = clock.add(duration)
    return str(result.hours()) + ":" + str(result.minutes()) + " PM"


class Time:
    def __init__(self, hours, minutes):
        self._hour = int(hours)
        self._minutes = int(minutes)

    def hours(self):
        return self._hour

    def minutes(self):
        return self._minutes

    def add(self, time):
        return Time(self.hours() + time.hours(), self.minutes() + time.minutes())
