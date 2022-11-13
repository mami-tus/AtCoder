class City:
    def __init__(self, num: int) -> None:
        self.num = num

    def get_connected_cities(self, roads: list[tuple[int, int]]) -> list[int]:
        connected_cities = []
        for city_a, city_b in roads:
            if city_a == self.num:
                connected_cities.append(city_b)
            elif city_b == self.num:
                connected_cities.append(city_a)
        return connected_cities


n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

for num in range(1, n + 1):
    city = City(num)
    connected_cities = sorted(city.get_connected_cities(roads))
    connected_cities.insert(0, len(connected_cities))
    print(*connected_cities)
