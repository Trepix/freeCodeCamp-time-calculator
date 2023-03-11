class Time:
    def __init__(self, hours, minutes):
        self.hours = int(hours)
        self.minutes = int(minutes)

    def add(self, time: 'Time'):
        return Time(self.hours + time.hours, self.minutes + time.minutes)


class Clock:
    def __init__(self, time: Time, clock_format):
        self._time = time
        self._format = clock_format

    def add(self, time: Time):
        return Clock(self._time.add(time), self._format)

    def to_string(self):
        minutes = self._time.minutes % 60
        hours = self._time.hours + int(self._time.minutes / 60)
        clock_format = self._format
        if hours > 12:
            clock_format = "PM"
            hours -= 12
        return f'{hours}:{minutes:02} {clock_format}'


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
