def dog_years():
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

         #enter your code here   
    human_form_age = int(input("input a dog's age in human years: "))
    human_age = 20
    dog_age = 0

    if human_form_age > human_age:
        print("Dog's age in human age should not be greater than 20")
    elif human_form_age < 1:
        print("Please enter age in years not months")
    else:
        if human_form_age == 1:
            dog_age = 1 * 10.5
        elif human_form_age  > 1 or human_form_age <= 20:
                dog_age_ = 10.5
                dog_2_year_human = 2 * dog_age_
                human_year = human_form_age - 2
                results = human_year * 4
                dog_age = results + dog_2_year_human
    print(f"The dog's age in dog years is: {int(dog_age)}")

dog_years()

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to i. 
    But for multiples of three print “Fizz” instead of the iber, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

    #enter your code here
    outcome = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            outcome.append("FizzBuzz")
        elif i % 3 == 0:
            outcome.append("Fizz")
        elif i % 5 == 0:
            outcome.append("Buzz")
        else:
            outcome.append(i)
    print(outcome)
fizzbuzz(15) 

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    
    #enter your code here
    message = sentence.split()
    output = {}
    for word in message:
        output[word] = len(word)
    return output

sentence = input('Input a sentence: ')
Output = word_lengths(sentence)
print(Output)

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    
    #enter your code here
    cubed_num = []
    for cubed in str(number):
        num = int(cubed) **3
        cubed_num.append(num)
    print(cubed_num)
    
    total = sum(cubed_num)
    print(f"The cubed sum is {total}")

cube_sum(123)