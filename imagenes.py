import queue
import random
import threading
import time
from datetime import datetime

def producer(image_queue: queue.Queue, max_interval: float, sources: list):
    image_id = 1
    while True:
        time.sleep(random.uniform(0.0, max_interval))
        image = (
            image_id,
            random.choice(sources),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        image_queue.put(image)
        print(f"[RECEPCIÓN] Imagen {image[0]} de {image[1]} almacenada en cola.")
        image_id += 1

def consumer(image_queue: queue.Queue, processing_time: float):
    while True:
        item = image_queue.get()
        image_id, source, received_at = item
        print(f"[PROCESO] Iniciando imagen {image_id} de {source} recibida a las {received_at}.")
        time.sleep(random.uniform(0.5, processing_time))
        print(f"[PROCESO] Imagen {image_id} procesada.")
        image_queue.task_done()


def prompt_int(message: str, default: int) -> int:
    raw = input(f"{message} [{default}]: ").strip()
    if raw == "":
        return default
    try:
        value = int(raw)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print(f"Entrada no válida. Se usará el valor recomendado {default}.")
        return default


def prompt_float(message: str, default: float) -> float:
    raw = input(f"{message} [{default}]: ").strip()
    if raw == "":
        return default
    try:
        value = float(raw)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print(f"Entrada no válida. Se usará el valor recomendado {default}.")
        return default


def main():
    print("Configuración inicial del sistema de imágenes satelitales")
    queue_size = prompt_int("Tamaño de la cola FIFO (recomendado 10)", 10)
    max_producer_interval = prompt_float("Intervalo máximo de llegada de imágenes en segundos (recomendado 1.5)", 1.5)
    max_consumer_time = prompt_float("Tiempo máximo de procesamiento por imagen en segundos (recomendado 5)", 5.0)
    satellite_count = prompt_int("Número de satélites a simular (recomendado 3)", 3)
    consumer_count = prompt_int("Número de consumidores simultáneos (recomendado 2)", 2)

    sources = [f"Satélite {i + 1}" for i in range(satellite_count)]
    image_queue = queue.Queue(maxsize=queue_size)

    producer_thread = threading.Thread(
        target=producer,
        args=(image_queue, max_producer_interval, sources),
        daemon=True,
    )
    producer_thread.start()

    consumer_threads = []
    for i in range(consumer_count):
        thread = threading.Thread(
            target=consumer,
            args=(image_queue, max_consumer_time),
            daemon=True,
        )
        thread.start()
        consumer_threads.append(thread)

    print("Iniciando el sistema de recepción y procesamiento de imágenes...")
    print(f"Satélites en origen: {satellite_count}")
    print(f"Consumidores activos: {consumer_count}")
    print("Pulse Ctrl+C para detener el programa.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. El programa se detiene.")

if __name__ == "__main__":
    main()
