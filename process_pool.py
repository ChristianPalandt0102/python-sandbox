import multiprocessing as mp
import subprocess

PROCESSES = 5
SUBPROCESSES = 5

def worker(box, port, pid):

    children = []

    for i in range(SUBPROCESSES):
        p = subprocess.Popen(
            ["python3", "-c", "while True: pass"]
        )
        children.append(p)

    print(f"BOX{box} PORT{port} PROC{pid} running")

def spawn_port_workers(box, port):

    workers = []

    for pid in range(PROCESSES):
        p = mp.Process(
            target=worker,
            args=(box, port, pid)
        )
        p.start()
        workers.append(p)

    return workers
