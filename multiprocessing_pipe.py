import os
import multiprocessing

def proceso_lector(pipe):
    pid_lector = os.getpid()
    while True:
        mensaje = input()  # Leer línea de entrada estándar
        pipe.send((pid_lector, mensaje))  # Enviar mensaje al otro proceso

def proceso_mostrador(pipe):
    pid_mostrador = os.getpid()
    while True:
        pid, mensaje = pipe.recv()  # Recibir mensaje desde el otro proceso
        print(f"Leyendo (pid: {pid_mostrador}): {mensaje}")

if __name__ == "_main_":
    pipe = multiprocessing.Pipe()  # Crear pipe compartido

    # Crear proceso lector
    proceso_1 = multiprocessing.Process(target=proceso_lector, args=(pipe[1],))
    proceso_1.start()

    # Crear proceso mostrador
    proceso_2 = multiprocessing.Process(target=proceso_mostrador, args=(pipe[0],))
    proceso_2.start()

    # Esperar a que los procesos terminen (esto se ejecutará en bucle infinito)
    proceso_1.join()
    proceso_2.join()
