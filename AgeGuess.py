
print("I can guess your age!\nDon't believe me?")
n = int(input("Pick a number between 1-10: "))
m = (n * 2) + 5
o = m * 50
print("Has your birthday passed this year?")
n = int(input("Enter 1 for YES, 2 for NO: "))
if n == 1:
    p = o + 1769
if n == 2:
    p = o + 1768
print("So here's the thing, I've crunched some numbers and this is what I got so far %d" % p)
n = int(input("Trust me on this one, Enter your birth year: "))
m = p - n
y = m
while m >= 10:
        m = m / 10
z = y % 100
print("You're age is %d and the number you chose is %d" % (z, m))







