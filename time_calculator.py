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
    def __init__(self, time: Time, clock_format: str):
        if clock_format == "PM":
            time = time.add(Time(12, 0))

        self._time = time

    @staticmethod
    def __create__(time: Time):
        return Clock(time, "")

    def add(self, time: Time):
        time_after = self._time.add(time)
        hours = time_after.hours
        return Clock.__create__(Time(hours, time_after.minutes))

    def to_string(self):
        hours = self._time.hours

        clock_format = "AM" if hours < 12 else "PM"
        hours = hours if hours <= 12 else hours - 12

        return f'{hours}:{self._time.minutes:02} {clock_format}'


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
