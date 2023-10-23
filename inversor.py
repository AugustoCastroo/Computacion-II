import os
import sys

def invertir_linea(linea):
    return linea[::-1]

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "-f":
        print("Uso: python3 inversor.py -f archivo.txt")
        sys.exit(1)

    archivo = open(sys.argv[2], 'r')
    lineas = archivo.readlines()
    archivo.close()

    num_hijos = len(lineas)
    pipes = []

    for _ in range(num_hijos):
        pipe_padre, pipe_hijo = os.pipe()
        pipes.append((pipe_padre, pipe_hijo))

    for i in range(num_hijos):
        pid = os.fork()
        if pid == 0:  # Proceso hijo
            os.close(pipes[i][1])  # Cerramos el pipe de escritura del hijo
            linea = os.read(pipes[i][0], 1024).decode().strip()
            linea_invertida = invertir_linea(linea)
            os.write(pipes[i][0], linea_invertida.encode())
            os.close(pipes[i][0])
            sys.exit(0)
        else:  # Proceso padre
            os.close(pipes[i][0])  # Cerramos el pipe de lectura del padre
            os.write(pipes[i][1], lineas[i].encode())
            os.close(pipes[i][1])

    for _ in range(num_hijos):
        os.wait()

    for i in range(num_hijos):
        linea_invertida = os.read(pipes[i][0], 1024).decode().strip()
        print(f"Línea {i + 1} invertida: {linea_invertida}")
        os.close(pipes[i][0])

if __name__ == "__main__":
    main()

