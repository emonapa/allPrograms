
def function(x):
    return x**2

def integrate(a,b):
    sum = 0
    for i in range((b-a)**3):
        sum += function(a + i/(b-a)**2)
    sum *= 1/(b-a)**2
    return sum

print("mez 1: ")
a = int(input())
print("mez 2: ")
b = int(input())

print(integrate(a,b))
#working only for larger scale