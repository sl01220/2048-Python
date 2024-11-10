import sys
def get_card_value(card):
    if card == 1 or card == 14 or card == 27 or card == 40:
        return 14  # Ace can be high in certain cases
    return (card - 1) % 13 + 1


def get_hand_score(hand):
    values = sorted([get_card_value(card) for card in hand])
    suits = [((card - 1) // 13) for card in hand]
    value_counts = {value: values.count(value) for value in values}

    is_flush = len(set(suits)) == 1
    is_straight = values == list(range(values[0], values[0] + 5))
    is_straight_ace_low = values == [1, 2, 3, 4, 14]  # Ace can be low in a 5-high straight

    if is_flush and (is_straight or is_straight_ace_low):
        return 7  # Straight flush
    elif 4 in value_counts.values():
        return 6  # Four of a kind
    elif 3 in value_counts.values() and 2 in value_counts.values():
        return 5  # Full house
    elif is_straight or is_straight_ace_low:
        return 4  # Straight
    elif 3 in value_counts.values():
        return 3  # Three of a kind
    elif list(value_counts.values()).count(2) == 2:
        return 2  # Two pair
    elif 2 in value_counts.values():
        return 1  # One pair
    else:
        return 0  # High card


def main():
    for i in sys.stdin:
        lines=i.split()

    num_cases = int(lines[0])
    for i in range(1, num_cases + 1):
        hand = list(map(int, lines[i].split()))
        score = get_hand_score(hand)
        print(score)


if __name__ == "__main__":
    main()

