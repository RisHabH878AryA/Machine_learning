# Create a nested function that returns another function which multiplies by 'n'..

def wrapper_func(n):
    def protected_func(num):
        return num * n
    return protected_func

times_10 = wrapper_func(10)
times_20 = wrapper_func(20)

print(times_10(10))
print(times_20(20))