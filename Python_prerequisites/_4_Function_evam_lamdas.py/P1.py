# Write a function that takes any number of arguements and return the sum..
def sum_all_args(*args, **kwargs):
    print(args, kwargs)
    return (sum(args), sum(kwargs["my_list"]))

print(sum_all_args(1,2,3,4,5,6,7,8,9,10, my_list = [1,2,3]))
