class Time:
    def __init__(self, hours, minutes):
        self._hour = int(hours)
        self._minutes = int(minutes)

    def hours(self):
        return str(self._hour)

    def minutes(self):
        return f"{self._minutes:02}"

    def add(self, time: 'Time'):
        return Time(self._hour + time._hour, self._minutes + time._minutes)


class Clock:
    def __init__(self, time: Time, clock_format):
        self._time = time
        self._format = clock_format

    def add(self, time: Time):
        return Clock(self._time.add(time), self._format)

    def to_string(self):
        return f'{self._time.hours()}:{str(self._time.minutes())} {self._format}'


def parse_clock(start) -> Clock:
    time = start.split()[0].split(":")
    return Clock(Time(time[0], time[1]), "PM")


def parse_duration(duration):
    time = duration.split(":")
    return Time(time[0], time[1])


def add_time(start, duration):
    clock = parse_clock(start)
    duration = parse_duration(duration)
    clock = clock.add(duration)
    return clock.to_string()
