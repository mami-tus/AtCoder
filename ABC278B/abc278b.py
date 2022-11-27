from datetime import datetime, timedelta


class Clock:
    def __init__(self, time: datetime):
        self.time = time

    def is_misjudged_time(self):
        h_zero = str(self.time.hour).zfill(2)
        m_zero = str(self.time.minute).zfill(2)
        a, b, c, d = int(h_zero[0]), int(h_zero[1]), int(m_zero[0]), int(m_zero[1])
        if a * 10 + c <= 23 and b * 10 + d <= 59:
            return True
        else:
            return False


h, m = map(int, input().split())
clock = Clock(datetime(2020, 1, 1, h, m))

while True:
    if clock.is_misjudged_time():
        print(clock.time.hour, clock.time.minute)
        break
    elif 5 < clock.time.hour < 9 or 15 < clock.time.hour < 19:
        clock.time += timedelta(hours=1)
    else:
        clock.time += timedelta(minutes=1)
