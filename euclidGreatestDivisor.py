print("první číslo:")
n1 = int(input())

print("druhé číslo:")
n2 = int(input())

def euclid_gd(n1, n2):
    t = n1 % n2
    if t != 0:
        return euclid_gd(n2, t)
    else:
        return n2
    
print("nejvetěí společný dělitel je: " + str(euclid_gd(n1, n2)))



