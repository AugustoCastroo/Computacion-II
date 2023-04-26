import argparse
import os

parser = argparse.ArgumentParser(description='Copia el contenido de un archivo a otro')

parser.add_argument('-i', '--input', type=str, required=True,
                    help='nombre del archivo de entrada')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='nombre del archivo de salida')

args = parser.parse_args()

if not os.path.exists(args.input):
    print("El archivo de entrada no existe")
    exit(1)

with open(args.input, 'r') as f:
    contenido = f.read()

with open(args.output, 'w') as f:
    f.write(contenido)

print(f"Se ha copiado el contenido de {args.input} a {args.output}")
