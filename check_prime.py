def is_prime(num):
    for i in range(2, num):
        if(num%i) == 0:
            return False
    return True

num = int(input("Please Enter a number: "))

check_prime = is_prime(num)

if check_prime:
    print("Congrates! Your number is a Prime")
else:
    print("Your number is not a prime")