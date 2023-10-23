import os

def hijo():
    pid_hijo = os.getpid()
    for _ in range(5):
        print(f"Soy el hijo, PID {pid_hijo}")
    print(f"PID {pid_hijo} terminado")

def padre():
    pid_padre = os.getpid()
    pid_hijo = os.fork()

    if pid_hijo == 0:
        # Proceso hijo
        hijo()
    else:
        # Proceso padre
        for _ in range(2):
            print(f"Soy el padre, PID {pid_padre}, mi hijo es {pid_hijo}")
        os.wait()  # Esperar a que termine el hijo
        print(f"Mi proceso hijo, PID {pid_hijo}, terminó")

if __name__ == "__main__":
    padre()
