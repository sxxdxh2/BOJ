v = int(input())

a = input()

if a.count("A") > a.count("B"):
    print("A")
elif a.count("A") < a.count("B"):
    print("B")
else:
    print("Tie")
