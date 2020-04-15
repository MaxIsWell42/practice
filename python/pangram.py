alphabet = "abcdefghijklmnopqrstuvwxyz"

""" 
Psuedocode:
- Establish alphabet
- Check if it's over >= 26
- Convert to unicase
- Find each letter from the alphabet in the string

Other efficient data structures:
- Sets 
- Hashtables
"""

h = []
def is_pangram(string):
    if len(string) >= 26:
        string = string.lower()
        for letter in alphabet:
            if letter in string and letter not in h: 
                h.extend(letter)
                print(h)
                
        if len(h) == 26:
            return True
        
    return False

if __name__ == "__main__":
    s = "The quick brown fox jumps over the lazy dog"
    if is_pangram(s) == True:
        print("This is a pangram")
    else:
        print("This is not a pangram")
        
    # Bad inputs:
    # s = "The1quick1brown1fox1jumps1over1the1lazy1dog"
    # s = "()(*(*&(^&*^???{}abcdefghijklmnopqrstuvwxyz"