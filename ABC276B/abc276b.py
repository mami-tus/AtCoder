class City:
    def __init__(self, num: int, connected_cities: list[int]) -> None:
        self.num = num
        self.connected_cities = connected_cities


n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
cities = [City(num, []) for num in range(1, n + 1)]

for a, b in roads:
    city_a = cities[a - 1]
    city_b = cities[b - 1]
    city_a.connected_cities.append(city_b.num)
    city_b.connected_cities.append(city_a.num)
for city in cities:
    print(len(city.connected_cities), *sorted(city.connected_cities))
