C = float(input('Qual a temperatura em °C'))
F = (C * 1.8) + 32
print('A temperatura em {}°C convertida para Fahrenheit é {}°F'.format(C, F))

F2 = float(input('Qual a temperatua em °F'))
C2 = (F2 - 32) / 1.8
print('A temperatura em {}°F convertida para Celsius é {}°C'.format(F2, C2))
