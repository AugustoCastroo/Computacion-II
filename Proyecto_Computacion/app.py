import multiprocessing
import cmath

numeros = [] # Crear una lista vacía
while True: # Iniciar un bucle infinito
    numero = input("Ingrese un número complejo o presione ENTER para terminar: ") # Pedir un número al usuario
    if numero == "": # Si el usuario presiona ENTER
        break # Salir del bucle
    else: # Si el usuario ingresa algo
        try: # Intentar
            numero = complex(numero) # Convertir el número a un complejo
            numeros.append(numero) # Añadir el número a la lista
        except ValueError: # Si se produce una excepción
            print("No es un número complejo válido") # Mostrar un mensaje de error

def modulo_fase(numero, q):
    modulo = abs(numero)
    fase = cmath.phase(numero)
    q.put((modulo, fase))

def raiz_log(numero, q):
    raiz = cmath.sqrt(numero)
    log = cmath.log(numero)
    q.put((raiz, log))

q = multiprocessing.Queue()

procesos = []

for numero in numeros:
    p1 = multiprocessing.Process(target=modulo_fase, args=(numero, q))
    p2 = multiprocessing.Process(target=raiz_log, args=(numero, q))
    procesos.append(p1)
    procesos.append(p2)
    p1.start()
    p2.start()

for proceso in procesos:
    proceso.join()

resultados = []

while not q.empty():
    resultado = q.get()
    resultados.append(resultado)

print(resultados)

