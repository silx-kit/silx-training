# One possible solution
# hint for other solutions: 
#  - you could use a break in the while loop
#  - you could avoid accessing res last elements by defining other variables
res = [0, 1]
next_el = res[0] + res[1]
while next_el < 1000: 
    res.append(next_el)
    next_el = res[-2] + res[-1]