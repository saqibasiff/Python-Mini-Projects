# Normal Function

def double(x):
     return x * 2
print(double(5))

# LAMBDA FUNCTION

double = lambda x : x * 2

print(double(5))

# Long Example Lambda

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(map(lambda x: x ** 2, number))

print(result)

