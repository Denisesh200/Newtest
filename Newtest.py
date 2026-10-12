def perimetrs(a, b):
    return 2 * (a + b)

def laukums(a, b):
    return a * b

try:
    a = int(input("Ievadi garumu: "))
    b = int(input("Ievadi platumu: "))

    print("Perimetrs:", perimetrs(a, b))
    print("Laukums:", laukums(a, b))

except ValueError:
    print("Kļūda! Ievadi ciparus!")