class Card:
    def __init__(
        self,
        first_character: str,
        second_character: str,
    ) -> None:
        self.first_character = first_character
        self.second_character = second_character
        self.PLAYING_CARDS_TYPES = ["H", "D", "C", "S"]
        self.PLAYING_CARDS_NUMS = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "T",
            "J",
            "Q",
            "K",
        ]

    def is_playing_cards(self) -> bool:
        if (self.first_character in self.PLAYING_CARDS_TYPES) and (
            self.second_character in self.PLAYING_CARDS_NUMS
        ):
            return True
        else:
            return False


n = int(input())
cards = [input() for _ in range(n)]

if len(set(cards)) != len(cards):
    print("No")
    exit()
for c in cards:
    card = Card(c[0], c[1])
    if not card.is_playing_cards():
        print("No")
        exit()
print("Yes")
