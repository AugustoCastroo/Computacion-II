import os
import argparse
import multiprocessing

def proceso_hijo(pid, pid_padre):
        print(f"Soy el proceso {pid}, mi padre es {pid_padre}")

def main():
    parser = argparse.ArgumentParser(description="Generar N procesos hijos")
    parser.add_argument("-n", type=int, help="Número de procesos hijos a crear", required=True)
    args = parser.parse_args()

    num_procesos_hijos = args.n
    pid_padre = os.getpid()

    for i in range(1, num_procesos_hijos + 1):
        proceso = multiprocessing.Process(target=proceso_hijo, args=(i, pid_padre))
        proceso.start()
        proceso.join()

if __name__ == "__main__":
    main()

