import os
import signal
import multiprocessing

def proceso_a(pipe_ab, pipe_bc):
    pid_a = os.getpid()
    print(f"A (PID={pid_a}) esperando la señal USR1")

    # Esperar la señal USR1
    signal.pause()

    # Leer mensaje 1 de B
    mensaje1 = pipe_ab.recv()
    print(f"A (PID={pid_a}) leyendo:\n{mensaje1}")

    # Enviar señal USR2 a C
    os.kill(pid_c, signal.SIGUSR2)

    # Esperar la señal USR2
    signal.pause()

    # Leer mensaje 2 de C
    mensaje2 = pipe_bc.recv()
    print(f"A (PID={pid_a}) leyendo:\n{mensaje2}")

def proceso_b(pipe_ab, pipe_bc):
    pid_b = os.getpid()
    print(f"B (PID={pid_b})")

    # Enviar señal USR1 a A
    os.kill(pid_a, signal.SIGUSR1)

    mensaje1 = f"Mensaje 1 (PID={pid_b})\n"
    pipe_ab.send(mensaje1)

    # Esperar la señal USR1 de C
    signal.pause()

def proceso_c(pipe_ab, pipe_bc):
    pid_c = os.getpid()
    print(f"C (PID={pid_c}) esperando la señal USR2")

    # Esperar la señal USR2
    signal.pause()

    mensaje2 = f"Mensaje 2 (PID={pid_c})\n"
    pipe_bc.send(mensaje2)

if __name__ == "_main_":
    with multiprocessing.Manager() as manager:
        pipe_ab = manager.Pipe()
        pipe_bc = manager.Pipe()
        pid_a = os.getpid()

        # Crear proceso C
        proceso_c = multiprocessing.Process(target=proceso_c, args=(pipe_ab, pipe_bc))
        proceso_c.start()
        pid_c = proceso_c.pid

        # Crear proceso A
        proceso_a = multiprocessing.Process(target=proceso_a, args=(pipe_ab, pipe_bc))
        proceso_a.start()
        proceso_a.join()

        proceso_c.join()
