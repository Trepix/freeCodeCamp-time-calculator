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
        days = self._time.days
        match days:
            case 0:
                return ""
            case 1:
                return "(next day)"
            case _:
                return f"({self._time.days} days later)"

    def _format_hours_output(self):
        hours = self._time.hours
        match hours:
            case 0:
                return 12
            case hours if hours <= 12:
                return hours
            case _:
                return hours - 12

    def to_string(self):
        hours = self._format_hours_output()
        clock_format = "AM" if self._time.hours < 12 else "PM"

        time = f'{hours}:{self._time.minutes:02}'

        days = self._format_days_output()
        return f'{time} {clock_format} {days}'.rstrip()


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
