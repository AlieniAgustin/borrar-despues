# README - Preparar entorno para proyecto de Grafo y Rutas

Este README explica cómo configurar un entorno en Linux Mint para trabajar con **Python**, `osmnx` y `matplotlib`, y generar el grafo vial de Río Cuarto para pruebas de rutas y carpooling.

---

## 1️⃣ Requisitos previos

- Python 3 instalado:
```bash
python3 --version
```
Si no lo tenés:
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

---

## 2️⃣ Crear un entorno virtual

Se recomienda usar un **entorno virtual** para no afectar paquetes del sistema:
```bash
python3 -m venv ~/venvs/osmnx
```

---

## 3️⃣ Activar el entorno virtual

Cada vez que abras una nueva terminal, activá el entorno:
```bash
source ~/venvs/osmnx/bin/activate
```
> Al activarlo, el prompt debería mostrar algo así:
```
(osmnx) agustin@pc:~$
```

---

## 4️⃣ Actualizar pip e instalar librerías

Con el entorno activado, instalar paquetes necesarios:
```bash
pip install --upgrade pip
pip install osmnx matplotlib
```
- `osmnx` → descargar y generar grafos de OpenStreetMap.
- `matplotlib` → graficar el grafo en imágenes.

---

## 5️⃣ Probar la instalación

ejecutar prueba.py 

---

## 6️⃣ Salir del entorno virtual

Cuando termines de trabajar:
```bash
deactivate
```
- Volvés al Python del sistema.

---
