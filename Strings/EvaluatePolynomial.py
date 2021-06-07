#Time complexity = O(n^2) because pow(x,n) takes O(n) complexity and outer for loop runs O(n) times
#We can make this to O(nlogn) by doing pow() to O(logn)
def evaluate_polynomial(poly,n,x):
    result = 0
    exponent = n-1
    for i in range(1,n+1):
        print("poly = ",poly[i-1])
        result += pow(x,exponent)*poly[i-1]
        exponent -= 1
    return result

#Using Horner's Method we can do it in O(n) time complexity
#2x^3 -6x^2+2x-1 can be given as ----> ((2x-6)x+2)x-1
def evaluate_polynomial_horner_method(poly,n,x):
    res = poly[0]
    for i in range(1,n):
        res = res*x + poly[i]
    return res


poly = [2,-6,2,-1]
n=len(poly)
x=3
print(evaluate_polynomial(poly,n,x))
print(evaluate_polynomial_horner_method(poly,n,x))