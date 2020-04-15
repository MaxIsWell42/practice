# a = [2, 7, 8, 3, 11]
h = []
biggest = []

# Find the k largest values in an array of n numbers. Return them in a new array sorted in decreasing order.
    
def largest(a, k):
    i = 0
    if len(a) == 1:
        return a
    else:
        for _ in a:
            h.append(max(a))
            a.remove(max(a))
        while(k > 0):
            biggest.append(h[i])
            i += 1
            k -= 1
        return biggest

if __name__ == "__main__":
    # Test case
    a = [2, 7, 8, 11, 5, 4]
    k = 3
    x = largest(a, k)
    print(x)
    
    # Bad inputs
    # a = [2.0341234123412341234, 2/3, "string"]
    # a = []
    
    # k = -3
    # k = "nothing"
    # k = len(a) + 1
    # k =0
    
    # Edge cases
    # a = [-3]
    # k = [1]