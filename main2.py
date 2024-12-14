#map cunction concept
def square(n):
    return n*n
holding_cell=(0,-1,-2,-3)
super_new=map(square,holding_cell)
print(list(super_new))