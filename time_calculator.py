class Time:
    def __init__(self, hours, minutes):
        self._hour = int(hours)
        self._minutes = int(minutes)

    def hours(self):
        return self._hour

    def minutes(self):
        return self._minutes

    def add(self, time: 'Time'):
        return Time(self._hour + time._hour, self._minutes + time._minutes)


class Clock:
    def __init__(self, time: Time, clock_format):
        self._time = time
        self._format = clock_format

    def add(self, time: Time):
        return Clock(self._time.add(time), self._format)

    def to_string(self):
        minutes = self._time.minutes()
        return f'{self._time.hours()}:{minutes:02} {self._format}'


def parse_clock(start) -> Clock:
    time = start.split()[0].split(":")
    clock_format = start.split()[1]
    return Clock(Time(time[0], time[1]), clock_format)


def parse_duration(duration):
    time = duration.split(":")
    return Time(time[0], time[1])


def add_time(start, duration):
    clock = parse_clock(start)
    duration = parse_duration(duration)
    return clock.add(duration).to_string()
