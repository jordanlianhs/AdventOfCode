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


def strength(hand):
    hand = replace_cards(hand)
    # print(hand)
    C = count_cards(hand)
    # print(C)
    # print(C.values())
    # print(sorted(C.values()))
    return determine_hand_strength(C, hand)


def replace_cards(hand):
    '''
    Replace T, J, Q, K, A with 10, 11, 12, 13, 14 in terms of ASCII
    '''
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))
    return hand


def count_cards(hand):
    return Counter(hand)


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

'''
When the sorted function is used on a list of such tuples, it first sorts by the first element of each tuple (the hand strength).
If there is a tie, it sorts by the second element (the hand string).

In the case of "T55J5" and "QQQJA", both hands match the pattern (1, 1, 3), which represents a Three of a Kind. 
However, the sorting does not stop there.
If two hands have the same pattern, they are further sorted based on the cards that make up the Three of a Kind.
In ASCII, 'T' (representing 10) has a lower value than 'Q'. 
Therefore, "T55J5" (Three of a Kind with 5s) is considered weaker than "QQQJA" (Three of a Kind with Queens), 
and "QQQJA" will be placed before "T55J5" in the sorted list.

This is achieved by the determine_hand_strength function returning a tuple (strength, hand). 
When Python sorts a list of tuples, it first sorts by the first element of each tuple. 
If there is a tie, it sorts by the second element, and so on. In this case, the hand string itself is used as a tie-breaker, 
and since 'Q' comes before 'T' in ASCII, "QQQJA" comes before "T55J5".

By using the lambda function as the key argument in the sorted() function, we are telling it to sort 
the elements of H based on the strength of their first element, followed by the second element if there are ties, so on. 
The sorted() function will use the comparison key returned by the lambda function to determine the order of the elements in the sorted list.
'''
H = sorted(H, key=lambda hb: strength(hb[0]))

ans = 0
for i, (h, b) in enumerate(H):
    # print(i,h,b)
    ans += (i + 1) * int(b)
print(ans)
