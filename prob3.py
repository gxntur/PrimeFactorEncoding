"""
Compsci 320 Assignment 1, finding PFE prime factor encoding
Author: William Guntur
Problem 3.
Input: Space-seperated series of pf-encoded integers.
Output: A single line of the pf-encoding of the product of inputs.
"""
import re

def main():
    raw_input = input().strip()
    # Substitute multiple whitespace characters for a single space
    split_input = re.sub("\s\s+", " ",raw_input)
    split_input = split_input.split(' ')
    ints = []

    # If the only numbers input are 1's, onlyOnes is set to True
    onlyOnes = True
    for i in split_input:
        if i != '1':
            onlyOnes = False
        i.strip()
        pf = i.split('*')
        for j in pf:
            if '^' in j:
                temp = j.split('^')
                for k in range(int(temp[1])):
                    ints.append(int(temp[0]))
            else:
                ints.append(int(j))
            
    ints.sort()
    done = []
    done.append(1)
    result = ''
    if 0 in ints:
        result = 0
    elif onlyOnes:
        result = 1
    else:
        for j in ints:
            if j not in done:
                done.append(j)
                exp = ints.count(j)
                if exp >1:
                    result += str(j) + "^" + str(exp) + "*"
                else:
                    result += str(j) + "*"
        # Remove the last "*"
        result = result[:-1]
    print(result)
   

main()
