import os
from collections import Counter

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day7.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


def strength(hand):
    hand = replace_cards(hand)
    # print(hand)
    C = count_cards(hand)
    # print(C)
    target = find_target_card(C)
    # print(target)
    handle_special_case(C, target)
    # print(C)
    return determine_hand_strength(C, hand)


def replace_cards(hand):
    '''
    Replace T, J, Q, K, A with 10, 11, 12, 13, 14 in terms of ASCII
    '''
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))
    return hand


def count_cards(hand):
    return Counter(hand)


def find_target_card(C):
    '''
    finds the card that should be targeted to make the hand as strong as possible. 
    If there's a 'J' in the hand, it's not considered as the target unless it's the only card left.
    '''
    target = list(C.keys())[0]
    for k in C:
        # if the card is not '1' = 'J' and it's more frequent than the current target or the current target is '1' = 'J'
        if k != '1' and (C[k] > C[target] or (C[k] == C[target] and k > target) or target == '1'):
            target = k
    # Checks if the target is '1' = 'J' and if it is, checks if the only card in the hand is '1' = 'J' "JJJJJ"
    assert target != '1' or list(C.keys()) == ['1']
    return target


def handle_special_case(C, target):
    '''
    handles the special case where there's a 'J' in the hand and it's not the target card. 
    In this case, the count of 'J' is added to the target card's count and 'J' is removed from the count.
    '''
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


H = []
for line in file:
    hand, bid = line.split()
    H.append((hand, bid))
H = sorted(H, key=lambda hb: strength(hb[0]))
ans = 0
for i, (h, b) in enumerate(H):
    # print(i,h,b)
    ans += (i + 1) * int(b)
print(ans)
