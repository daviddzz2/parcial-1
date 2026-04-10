# parcial-1

Programa de ejemplo que simula la recepción y el procesamiento concurrente de imágenes satelitales usando el patrón Producer-Consumer con una cola FIFO.

## Ejecución

1. Asegúrate de tener Python 3 instalado.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:

```bash
python imagenes.py
```

Este programa genera imágenes de forma indefinida y las procesa usando una cola FIFO. El programa se ejecuta hasta que lo detengas con Ctrl+C.

Si quieres cambiar los valores, edita las variables dentro de `imagenes.py`:

- `queue_size`
- `max_producer_interval`
- `max_consumer_time`
