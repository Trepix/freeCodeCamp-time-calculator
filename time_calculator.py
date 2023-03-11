class Time:
    def __init__(self, hours, minutes):
        self.hours = int(hours)
        self.minutes = int(minutes)

    def add(self, time: 'Time'):
        hours = self.hours + time.hours
        minutes = self.minutes + time.minutes

        hours = hours + int(minutes / 60)
        minutes = minutes % 60
        return Time(hours, minutes)


class Clock:
    def __init__(self, time: Time, clock_format):
        self._time = time
        self._format = clock_format

    def add(self, time: Time):
        time_after = self._time.add(time)
        hours = time_after.hours
        clock_format = self._format
        if time_after.hours > 12:
            clock_format = "PM"
            hours -= 12
        return Clock(Time(hours, time_after.minutes), clock_format)

    def to_string(self):
        return f'{self._time.hours}:{self._time.minutes:02} {self._format}'


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
