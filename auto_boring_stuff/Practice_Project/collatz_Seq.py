
def collatz(number):        #even
    if (number % 2) == 0:
        print(number // 2)
        return(number // 2)
    elif (number % 2) == 1:     #odd
        result = (3 * number + 1)
        print(result)
        return(result)

n = input("Please enter a number: ")

collatz(int(n))

while n != 1:
    try:
        n = collatz(int(n))
    except:
        print("Error: Bad Input")
        break