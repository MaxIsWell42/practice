# a = [2, 7, 8, 3, 11]
h = []
biggest = []

    
def largest(a, k):
    i = 0
    if len(a) == 1:
        return a
    else:
        for num in a:
            h.append(max(a))
            a.remove(max(a))
        while(k > 0):
            biggest.append(h[i])
            i += 1
            k -= 1
        return biggest

if __name__ == "__main__":
    a = [2, 7, 8, 11, 5, 4]
    k = 3
    x = largest(a, k)
    print(x)
    