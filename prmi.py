def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def main():
   
   
    # user's name
    
    name = input("Enter your name: ")

    
    # Three favorite numbers
    
    numbers = []
    for i in range(3):
        num = int(input(f"Enter your {['first', 'second', 'third'][i]} favorite number: "))
        numbers.append(num)

    
    # favourite Numbers
    
    print(f"\nHello, {name}! Let's explore your favourite numbers:")

    
    #  Check if the numbers are even or odd and store in a list of tuples
   
   
    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

    
    #  Display even or odd status
    
    
    for num, status in even_odd_info:
        print(f"The number {num} is {status}.")

    
    # Calculating squares and display in a creative format
    
    
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num**2})")

    # Calculating the sum of the numbers
    
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    
    # Check if the sum is a prime number
   
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")    
if __name__ == "__main__":
    main()
