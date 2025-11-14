
# Optimización Numérica — Métodos de Búsqueda

Este proyecto consiste en una aplicación de optimización numérica con diversos métodos de búsqueda, como:

- Búsqueda Local
- Método de Fibonacci
- Método de Armijo
- Método de Wolfe

## Requisitos

### 1. Instalar dependencias

Asegúrate de tener el archivo `requirements.txt` en la raíz del proyecto. Este archivo incluye todas las bibliotecas necesarias para que el proyecto funcione correctamente.

### 2. Instalar dependencias desde `requirements.txt`

Abre la terminal y navega hasta la carpeta del proyecto. Luego, ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 3. Instalar PyQt6

Este proyecto utiliza **PyQt6** para la interfaz gráfica de usuario (GUI). Asegúrate de que esté instalado en tu entorno Python.

Para instalar **PyQt6**, ejecuta el siguiente comando:

```bash
pip install PyQt6
```

### 4. Instalar Matplotlib (si no lo tienes)

La aplicación usa **Matplotlib** para generar gráficos. Si aún no lo has instalado, ejecuta:

```bash
pip install matplotlib
```

### 5. Instalar dependencias adicionales

Si estás trabajando en un entorno Linux, asegúrate de instalar **Tkinter** (aunque en este proyecto no se utiliza directamente, es una posible dependencia por otros casos de uso). Puedes instalarlo con:

```bash
sudo apt-get install python3-tk
```

---

## Ejecución del programa

### 1. Ejecutar el programa desde el código fuente

Para ejecutar el programa en modo desarrollo (desde el código fuente), simplemente navega hasta la carpeta del proyecto y ejecuta:

```bash
python main.py
```

### 2. Ejecutar la versión compilada (archivo `.exe`)

Si has compilado el proyecto en un archivo ejecutable `.exe` utilizando PyInstaller, solo necesitas hacer doble clic en el archivo `main.exe` ubicado en la carpeta `dist/`, o ejecutarlo desde la terminal con el siguiente comando:

```bash
./dist/main.exe
```

La interfaz se abrirá directamente, sin necesidad de tener Python o las dependencias instaladas en el sistema destino.

---

## Funcionalidad

La aplicación permite realizar optimización numérica mediante los siguientes métodos de búsqueda:

1. **Búsqueda Local**: Un método para encontrar el mínimo o máximo de una función en un intervalo determinado.
2. **Método de Fibonacci**: Utiliza la secuencia de Fibonacci para determinar el paso óptimo en la búsqueda de extremos de una función.
3. **Método de Armijo**: Una técnica basada en el descenso de gradiente con búsqueda de paso, que utiliza la condición de Armijo para encontrar la tasa de aprendizaje.
4. **Método de Wolfe**: Un método de búsqueda lineal que utiliza condiciones de Wolfe para asegurar una búsqueda más eficiente del mínimo de la función.

Cada uno de estos métodos se presenta en una pestaña separada en la interfaz gráfica.

---

## Notas

- Este proyecto usa **PyQt6** para la interfaz gráfica.
- Asegúrate de tener todas las dependencias instaladas correctamente antes de ejecutar el proyecto.
- Si tienes problemas con la ejecución en tu sistema, no dudes en abrir un *issue* en el repositorio.

---

### Proyecto en desarrollo
Este proyecto está en constante mejora y expansión, así que espera nuevas funcionalidades y optimizaciones en el futuro.

---

### Licencia

Este proyecto se distribuye bajo la licencia GPL-3.0-only.

