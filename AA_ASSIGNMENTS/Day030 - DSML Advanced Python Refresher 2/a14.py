from functools import reduce 
def func(ints, names, numbers):
    
    # Use map to print the square of each numbers
    # Use filter to print only the names that are less than or equal to seven letters
    # Use reduce to print the product of these numbers
    
    # Complete all the three codes.

    
    map_result = list(map(lambda x:x*x, ints))
    filter_result = list(filter(lambda name: len(name)<=7, names))
    reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

    return map_result, filter_result, reduce_result
    