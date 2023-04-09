# FizzBuzz function
def FizzBuzz(start, finish):
    """
    Returns a list of strings where each string is either:
    - 'Fizz' if the number is divisible by 3
    - 'Buzz' if the number is divisible by 5
    - 'FizzBuzz' if the number is divisible by both 3 and 5
    - the number itself as a string otherwise

    Args:
        start (int): The first number in the range.
        finish (int): The last number in the range (inclusive).

    Returns:
        list: A list of FizzBuzz strings.
    """
    outlist = []
    for i in range(start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            outlist.append('FizzBuzz')
        elif i % 3 == 0:
            outlist.append('Fizz')
        elif i % 5 == 0:
            outlist.append('Buzz')
        else:
            outlist.append(str(i))
    return outlist

# Test Values
outlist = FizzBuzz(40, 45)
print(outlist)
