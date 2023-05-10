import argparse
import os

def calcular_suma_pares(pid):
    suma = 0
    for i in range(0, pid+1, 2):
        suma += i
    return suma

def main():
    parser = argparse.ArgumentParser(description='Programa que genera procesos hijos para calcular la suma de todos los números enteros pares entre 0 y su número de PID.')
    parser.add_argument('-n', type=int, help='Número de procesos hijos a generar.')
    parser.add_argument('-v', action='store_true', help='Habilitar modo verboso.')
    args = parser.parse_args()

    if args.n:
        for i in range(args.n):
            pid = os.fork()
            if pid == 0:
                if args.v:
                    print(f'Proceso hijo {i} iniciado.')
                suma_pares = calcular_suma_pares(os.getpid())
                print(f'{os.getpid()} - {os.getppid()}: {suma_pares}')
                if args.v:
                    print(f'Proceso hijo {i} finalizado.')
                exit(0)
        for i in range(args.n):
            os.wait()
    else:
        parser.print_help()

if __name__ == '_main_':
    main()
