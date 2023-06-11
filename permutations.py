# Write a solution that will print all permutations of a string.
# A permutation is an act of changing the arrangement of characters.
# Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

#
# def swap(ch, i, j):
#     temp = ch[i]
#     ch[i] = ch[j]
#     ch[j] = temp
#
# def permutations(ch, curr_index=0):
#     if curr_index == len(ch) - 1:
#         print(''.join(ch))
#
#     for i in range(curr_index, len(ch)):
#         swap(ch, curr_index, i)
#         permutations(ch, curr_index+1)
#         swap(ch, curr_index, i)
#
# string = 'ABC'
# print(permutations(list(string)))


def permutations(remaining, candidate=''):
    if len(remaining) == 0:
        print(candidate)

    for i in range(len(remaining)):
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:]
        permutations(newRemaining, newCandidate)

str = 'ABC'
print(permutations(str))
