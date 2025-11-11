def isPal(x):
    # Assumes x is a list
    # Returns true if the list is a palindrome; false otherwise
    temp = x[:]
    temp.reverse() 
    
    if temp == x:
        return True
    else:
        return False

def silly(n):
    # Assumes n is an int > 0
    # Gets n inputs from the user
    # Prints 'yes' if the sequence of inputs forms a palindrome;
    # 'no' otherwise
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
