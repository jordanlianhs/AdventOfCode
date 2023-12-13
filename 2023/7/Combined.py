import os
from collections import Counter

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "test.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


def strength(hand, part2):
    hand = replace_cards(hand, part2)
    print(hand)
    C = count_cards(hand)
    if part2:
        target = find_target_card(C)
        handle_special_case(C, target)
    return determine_hand_strength(C, hand)


def replace_cards(hand, part2):
    '''
    Replace T, J, Q, K, A with 10, 11, 12, 13, 14 in terms of ASCII
    '''
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1) if part2 else chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))
    return hand


def count_cards(hand):
    return Counter(hand)


def find_target_card(C):
    target = list(C.keys())[0]
    for k in C:
        if k != '1':
            if C[k] > C[target] or target == '1':
                target = k
    assert target != '1' or list(C.keys()) == ['1']
    return target


def handle_special_case(C, target):
    if '1' in C and target != '1':
        C[target] += C['1']
        del C['1']
    assert '1' not in C or list(C.keys()) == ['1'], f'{C} {hand}'


def determine_hand_strength(C, hand):
    sorted_values = sorted(C.values())
    if sorted_values == [5]:
        return (10, hand)
    elif sorted_values == [1, 4]:
        return (9, hand)
    elif sorted_values == [2, 3]:
        return (8, hand)
    elif sorted_values == [1, 1, 3]:
        return (7, hand)
    elif sorted_values == [1, 2, 2]:
        return (6, hand)
    elif sorted_values == [1, 1, 1, 2]:
        return (5, hand)
    elif sorted_values == [1, 1, 1, 1, 1]:
        return (4, hand)
    else:
        assert False, f'{C} {hand} {sorted_values}'


for part2 in [False, True]:
    H = []
    for line in file:
        hand, bid = line.split()
        H.append((hand, bid))
    H = sorted(H, key=lambda hb, part2=part2: strength(hb[0], part2))
    ans = 0
    for i, (h, b) in enumerate(H):
        # print(i,h,b)
        ans += (i + 1) * int(b)
    print(ans)
