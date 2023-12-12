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
    lines = S.split('\n')[1:] # throw away name
    # dst src sz
    self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    # print("tuples:", self.tuples)

  # list of [start, end) ranges
  def apply_range(self, R):
    A = []
    for (dest, src, sz) in self.tuples:
      src_end = src+sz
      NR = []
      while R:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = R.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,src))
        inter = (max(st, src), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          NR.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-src+dest, inter[1]-src+dest))
        if after[1]>after[0]:
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
i=0
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
  i+=1
  print(i, R)
  P2.append(min(R)[0])
print(min(P2))