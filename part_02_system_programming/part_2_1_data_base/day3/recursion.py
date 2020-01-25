def fun01(a):
    if a <= 1:
        return 1
    return a * fun01(a - 1)

print("n! = ",fun01(6))
