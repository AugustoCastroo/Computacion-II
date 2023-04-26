import sys
import getopt

operador = None
num1 = None
num2 = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "o:n:m:", ["operador=", "numero1=", "numero2="])
except getopt.GetoptError:
    print("calc.py -o <operador> -n <numero1> -m <numero2>")
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-o", "--operador"):
        if arg in ('+', '-', '*', '/'):
            operador = arg
        else:
            print("Operador inválido")
            sys.exit(2)
    elif opt in ("-n", "--numero1"):
        if arg.isdigit():
            num1 = int(arg)
        else:
            print("El primer número no es un entero")
            sys.exit(2)
    elif opt in ("-m", "--numero2"):
        if arg.isdigit():
            num2 = int(arg)
        else:
            print("El segundo número no es un entero")
            sys.exit(2)

if operador is None or num1 is None or num2 is None:
    print("calc.py -o <operador> -n <numero1> -m <numero2>")
    sys.exit(2)

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
else:
    resultado = num1 / num2

print(f"{num1} {operador} {num2} = {resultado}")
