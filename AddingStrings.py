# define the main function
def main():
    # get the users input of what numbers they want added together.
    stringOfNumbers = input('Enter a series of single-digit numbers: ')
    string_sum(stringOfNumbers)
    # set total to what the function string_sum returns
    total = string_sum(stringOfNumbers)
    # print results.
    print('The sum of', stringOfNumbers,'is', total)

def string_sum(stringOfNumbers):
    # set total to 0
    total = 0
    for ch in stringOfNumbers:
        # int each character and add it to the total
        total += int(ch)
    # return the total value
    return total
 
# Invoke main
main()
