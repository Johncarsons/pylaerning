# Legiblity to vote
name = input("What is your name? ")
print(f"Hello, {name}. Lets see if you are Legible for voting")
age = int(input("How old are you? "))
if age >= 18:
    print(f"{name} You are Legible for voting")
else:
    print(f"{name} You are not Legible for voting")
