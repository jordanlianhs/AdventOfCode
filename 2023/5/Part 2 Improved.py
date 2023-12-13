import os
# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day5.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

seed, *others = file
seed = [int(x) for x in seed.split(':')[1].split()]
# print(seed)
# print(others)


class Function:
    def __init__(self, S):
        lines = S.split('\n')[1:]  # throw away name
        # dst src sz
        self.tuples: list[tuple[int, int, int]] = [
            [int(x) for x in line.split()] for line in lines]
        # print("tuples:", self.tuples)

    # list of [start, end) ranges
    def apply_range(self, R):
        '''
        The apply_range function in the Function class is applying a series of transformations to a set of ranges. 
        Each transformation is defined by a tuple in self.tuples, which contains three integers: dest, src, and sz.

        Here's a step-by-step explanation of the transformation:

        For each tuple (dest, src, sz), calculate src_end as src + sz. This defines a sub-range [src, src_end) within the original range.

        For each range (st, ed) in R, split it into three parts: before, inter, and after.

        before is the part of the range before src. It is defined as (st, min(ed, src)).
        inter is the part of the range that intersects with [src, src_end). It is defined as (max(st, src), min(src_end, ed)).
        after is the part of the range after src_end. It is defined as (max(src_end, st), ed).
        If before is a valid range (i.e., its end is greater than its start), append it to NR.

        If inter is a valid range, transform it by subtracting src and adding dest to both its start and end, and then append the transformed range to A.

        If after is a valid range, append it to NR.

        After all ranges in R have been processed, R is replaced with NR, and the function moves on to the next tuple in self.tuples.

        In this Python code, NR and A are lists that are used to store ranges during the transformation process in the apply_range function.
        NR (New Ranges): This list is used to store the 'before' and 'after' parts of each range in R that are not affected by the current transformation. These parts are kept for further transformations in the next iterations of the loop over self.tuples.
        A (Adjusted ranges): This list is used to store the 'inter' parts of the ranges that are affected by the current transformation. For each 'inter' part, it is transformed by subtracting src and adding dest to both its start and end, and then the transformed range is appended to A.
        At the end of the function, A and R are concatenated and returned. This result contains all the transformed 'inter' parts of the ranges (in A), and all the 'before' and 'after' parts that were not affected by any transformation (in R).
        '''
        A = []
        for (dest, src, sz) in self.tuples:
            src_end = src+sz
            NR = []
            while R:
                # [st                                     ed)
                #          [src       src_end]
                # [BEFORE ][INTER            ][AFTER        )
                (st, ed) = R.pop()
                # (src,sz) might cut (st,ed)
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0]-src+dest, inter[1]-src+dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A+R


'''
same as
Fs = []
for s in others:
  Fs.append(Function(s))
'''
Fs = [Function(s) for s in others]
P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
# print(pairs)
i = 0
for st, sz in pairs:
    # inclusive on the left, exclusive on the right
    # e.g. [1,3) = [1,2]
    # length of [a,b) = b-a
    # [a,b) + [b,c) = [a,c)
    R = [(st, st+sz)]
    for f in Fs:
        R = f.apply_range(R)
#   print(len(R))
#   print(R)
    i += 1
    print(i, R)
    P2.append(min(R)[0])
print(P2)
print(min(P2))
