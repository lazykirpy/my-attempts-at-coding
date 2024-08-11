print("input a number, I'll check if it's a prime number or not!")

def prime(num):
    s = 2
    while s != num:
        if num % s == 0:
            print("is NOT a prime")
            break
        elif s == num-1:
            print("is a prime")
            break
        else:
            s = s + 1
while True:
    i = int(input())
    prime(i)
