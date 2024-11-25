def factorial(x): 
    #base code
    if x <= 1:
        return 1 
    
    else:
        return x * factorial(x-1)


for i in range(1, 11): 
    print(f"{i}! = {factorial(i)}")



def fibonacci(x):
    #base code
    if x<= 1:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
for i in range(1, 11):
    print(f"fib({i}) = {fibonacci(i)}")

def prepare_string(input_string):
    output_string = ""
    for c in input_string:
        if c.isalpha():
            output_string += c.lower()
    return output_string

test_string = "Go hang a salami, I'm a lasagna hog."

def is_palindrome(s):
    # base code 
    if len(s) <= 1:
        return True 
    
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
         
print(is_palindrome(prepare_string(test_string)))

def hanoi_solver(start, end, helper, disks):
    if disks == 0:
        return
    else:
        hanoi_solver(start, helper, end, disks-1)
        # solve disks -1 start to helper 
        print(f"Move disk from {start} to {end}")
        # solve disks - 1 from helper to end 
        hanoi_solver(helper, end, start, disks-1)

hanoi_solver("A","C", "B", 3)


        