import cmath
def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c
def find_roots(a, b, c):
    D = calculate_discriminant(a, b, c)  
    if D > 0:
        root1 = (-b + cmath.sqrt(D)) / (2 * a)
        root2 = (-b - cmath.sqrt(D)) / (2 * a)
        return (root1, root2)
    elif D == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        return None  # У уравнения нет действительных корней
# Пример использования
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число  c: "))

roots = find_roots(a, b, c)

if roots is None:
    print("У уравнения нет действительных корней.")
else:
    print("Корни уравнения:", roots)
