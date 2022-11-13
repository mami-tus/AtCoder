class Card:
    def __init__(
        self,
        first_character: str,
        second_character: str,
    ) -> None:
        self.first_character = first_character
        self.second_character = second_character

    def is_playing_cards(
        self,
        playing_cards_types: list[str],
        playing_cards_nums: list[str],
    ) -> bool:
        if (self.first_character in playing_cards_types) and (
            self.second_character in playing_cards_nums
        ):
            return True
        else:
            return False


n = int(input())
cards = [input() for _ in range(n)]
playing_cards_types = ["H", "D", "C", "S"]
playing_cards_nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
if len(set(cards)) != len(cards):
    print("No")
    exit()
for c in cards:
    card = Card(c[0], c[1])
    if not card.is_playing_cards(playing_cards_types, playing_cards_nums):
        print("No")
        exit()
print("Yes")
