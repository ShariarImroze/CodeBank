def fizzBuzz(n):
    # Write your code here
    n = list(range(1,n+1))
    for i in n: 
        if i % 3 == 0 & i % 5 == 0: 
            print('FizzBuzz')
        elif i % 3 == 0: 
            print('Fizz')
        elif i % 5 == 0: 
            print('Buzz')
        else: 
            print(i)