class Time:
    def __init__(self, hours, minutes):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.days = 0

    @staticmethod
    def __create__(days, hours, minutes):
        time = Time(hours, minutes)
        time.days = days
        return time

    def add(self, time: 'Time'):
        hours = self.hours + time.hours
        minutes = self.minutes + time.minutes

        days = int((hours + int(minutes / 60)) / 24)
        hours = (hours + int(minutes / 60)) % 24
        minutes = minutes % 60
        return Time.__create__(days, hours, minutes)


class Clock:
    def __init__(self, time: Time, clock_format: str):
        if clock_format == "PM":
            time = time.add(Time(12, 0))

        self._time = time

    def add(self, time: Time):
        return Clock(self._time.add(time), "")

    def _format_days_output(self):
        days = ""
        if self._time.days == 1:
            days = " (next day)"

        return days

    def to_string(self):
        hours = self._time.hours

        clock_format = "AM" if hours < 12 else "PM"
        hours = hours if hours <= 12 else hours - 12

        time = f'{hours}:{self._time.minutes:02} {clock_format}'
        days = self._format_days_output()

        return time + days


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
