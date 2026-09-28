temperatura = float(input("Informe a temperatura: "))
if temperatura < 20:
    print("Está frio!")
elif temperatura >= 20 and temperatura <= 28:
    print("Normal!")
else:
    print("Está quente!")