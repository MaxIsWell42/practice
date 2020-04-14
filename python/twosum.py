# a = [2, 7, 8, 11]
# target = 15

# Use sorting outside of memory(external sorting), count from beginning and end of array
# If the sum of pair is > than target, decrease the end number index by 1. If <, increase the beginning index by 1

def sum(a, target):
    h = {}
    for i, num in enumerate(a):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]