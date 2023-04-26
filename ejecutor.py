import argparse
import subprocess
import os
import datetime

parser = argparse.ArgumentParser(description='Ejecutar un comando y guardar su salida y log')
parser.add_argument('-c', '--command', type=str, required=True,
                    help='comando a ejecutar')
parser.add_argument('-f', '--output_file', type=str, required=True,
                    help='archivo donde se guarda la salida')
parser.add_argument('-l', '--log_file', type=str, required=True,
                    help='archivo donde se guarda el log')

args = parser.parse_args()

if not os.path.exists(args.output_file):
    open(args.output_file, 'a').close()

if not os.path.exists(args.log_file):
    open(args.log_file, 'a').close()

date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
    output = subprocess.check_output(args.command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    with open(args.output_file, 'a') as f:
        f.write(output)
    with open(args.log_file, 'a') as f:
        f.write(f"{date_time}: Comando \"{args.command}\" ejecutado correctamente\n")
except subprocess.CalledProcessError as e:
    with open(args.log_file, 'a') as f:
        f.write(f"{date_time}: {e.output.strip()}\n")
