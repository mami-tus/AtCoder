import datetime


class Clock:
    def __init__(self, time: datetime.datetime):
        self.time = time

    def is_misjudged_time(self):
        h_zero = str(self.time.hour).zfill(2)
        m_zero = str(self.time.minute).zfill(2)
        a, b, c, d = (
            h_zero[0],
            h_zero[1],
            m_zero[0],
            m_zero[1],
        )
        a, b, c, d = int(a), int(b), int(c), int(d)
        if a * 10 + c <= 23 and b * 10 + d <= 59:
            return True
        else:
            return False


h, m = map(int, input().split())
clock = Clock(datetime.datetime(2020, 1, 1, h, m))

while True:
    if clock.is_misjudged_time():
        print(clock.time.hour, clock.time.minute)
        break
    else:
        clock.time += datetime.timedelta(minutes=1)
