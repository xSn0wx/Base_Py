def operation_speciale(a = ""):
    if isinstance(a, int | float): # or isinstance(a, float):
        return a * a
    print("Mauvais type")
    return None

print(operation_speciale(5))