class City:
    def __init__(self, num: int, connected_cities: list[int]) -> None:
        self.num = num
        self.connected_cities = connected_cities


n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

for num in range(1, n + 1):
    connected_cities = []
    for city_a, city_b in roads:
        if city_a == num:
            connected_cities.append(city_b)
        elif city_b == num:
            connected_cities.append(city_a)
    city = City(num, connected_cities)
    connected_cities = sorted(city.connected_cities)
    print(len(connected_cities), *connected_cities)
