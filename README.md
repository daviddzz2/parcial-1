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

Al iniciar, el programa preguntará al usuario por los valores de configuración y ofrecerá recomendaciones predeterminadas:

- tamaño de la cola FIFO
- intervalo máximo de llegada de imágenes
- tiempo máximo de procesamiento por imagen
- número de satélites simulados
- número de consumidores simultáneos
