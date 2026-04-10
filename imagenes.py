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

def main():
    queue_size = 10
    max_producer_interval = 1.5
    max_consumer_time = 5

    image_queue = queue.Queue(maxsize=queue_size)
    sources = ["Satélite A", "Satélite B", "Satélite C"]

    producer_thread = threading.Thread(
        target=producer,
        args=(image_queue, max_producer_interval, sources),
        daemon=True,
    )
    consumer_thread = threading.Thread(
        target=consumer,
        args=(image_queue, max_consumer_time),
        daemon=True,
    )

    print("Iniciando el sistema de recepción y procesamiento de imágenes...")
    producer_thread.start()
    consumer_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. El programa se detiene.")

if __name__ == "__main__":
    main()
