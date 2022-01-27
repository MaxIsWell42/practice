# String S has characters followed by their frequency 
# Some characters appear twice
# Add all frequencies and return
# Example: a3c9b2c1
#   Since it has two instances of c, they should be added and the string returned as:
#   a3c10b2

from posixpath import split
import re

def betterCompression(s: str):
    vals = {}
    res = ""
    
    # Split into array of letters and numbers
    splitList = re.split('(\d+)', s)
    splitList.pop()
    # ['a', '3', 'c', '9', 'b', '2', 'c', '1']
    
    for i in range(len(splitList)-1):
        # If the value already exists, add to it by the frequency of this new instance
        # This never triggers for some reason
        if splitList[i] in vals:
            currFreq = splitList[i+1]
            print("Current Frequency: {}".format(currFreq))
            print(splitList[i])
            vals[splitList[i]] += currFreq
            
        # If it doesn't, create it
        # Something in here is messing up, causing all keys to be incremented numbers(1,2,3...)
        else:
            vals[i] = splitList[i+1]
            
    # Turn the dictionary back into a string
    for key in vals:
        print('Current Key: {}'.format(key))
        print('Current dictionary: {}'.format(vals))
        res += str(key)
        res += vals.get(key)
    
    
    
    return res  

if __name__ == "__main__":
    s = "a3c9b2c1"
    print(betterCompression(s))