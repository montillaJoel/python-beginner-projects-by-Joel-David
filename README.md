# Mis primeros proyectos en Python

Seis programas independientes que escribí para practicar Python en la terminal. Para probar uno, elige su comando en la tabla y sigue las indicaciones en inglés.

## Cómo ejecutarlos

Necesitas Python 3.6 o superior. Los seis programas usan solo la biblioteca estándar de Python.

Descarga el repositorio desde **Code → Download ZIP** y descomprímelo, o clónalo con Git:

```sh
git clone https://github.com/montillaJoel/python-beginner-projects-by-Joel-David.git
```

Abre una terminal dentro de la carpeta que contiene los archivos `.py`. En Windows usa los comandos de la tabla. En macOS o Linux sustituye `py -3` por `python3`.

| Programa | Cómo usarlo | Comando |
| --- | --- | --- |
| [Lista de tareas](to-do.py) | Escribe una tarea por línea. Introduce `exit` para ver la lista numerada y `n` para terminar. | `py -3 to-do.py` |
| [Adivina el número](Guess-My-Number.py) | Introduce un número y sigue las pistas «más alto» o «más bajo». Tienes diez intentos. El código puede elegir del 0 al 21, aunque el mensaje inicial indica 20. | `py -3 Guess-My-Number.py` |
| [Calculadora](calc.py) | Introduce dos números enteros y elige una operación: `+`, `-`, `*` o `/`. | `py -3 calc.py` |
| [Conversor de temperatura](unit-temp.py) | Introduce una temperatura entera en grados Celsius para obtener su equivalente en Fahrenheit. Por ejemplo, `25` devuelve `77.0`. | `py -3 unit-temp.py` |
| [Generador de contraseñas](passwords-generator.py) | Elige una longitud de al menos 3 para obtener una cadena con letras, dígitos y símbolos. Con menos de 3, el programa sigue intentando. Es un ejercicio con el módulo `random`. | `py -3 passwords-generator.py` |
| [Alarma de consola](simple-alarm.py) | Introduce la hora en formato de 12 horas, los minutos y `AM` o `PM`. Deja la terminal abierta para ver el aviso cuando llegue la hora local elegida. | `py -3 simple-alarm.py` |
