# Description

# Alice and Bob created one problem each for a coding contest.

# A reviewer rates the two challenges using 3 categories.
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

Alice = 0
Bob = 0
if len(list1)>=len(list2):
    n = len(list1)
else:
    n = len(list2)

for i in range(n):
    if list1[i]>list2[i]:
        Alice+=1
    elif list1[i]<list2[i]:
        Bob+=1
print(Alice,Bob)