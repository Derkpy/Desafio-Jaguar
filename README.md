# 🐆 Desafio-Jaguar
**Desafio-Jaguar** es una aplicación de escritorio de alto impacto, utilizada oficialmente en eventos universitarios para la carrera de Ingeniería en Sistemas Computacionales (ISC). El sistema evalúa conocimientos técnicos de forma dinámica y gamificada.
## 🕹️ Dinámica del Juego
- **Evaluación por Materias:** El sistema extrae preguntas aleatorias de una base de datos SQL categorizadas por materia.
- **Flujo Dinámico:** 
  - Si el usuario acierta, se desbloquea una **adivinanza** y se avanza a la siguiente materia.
  - Si el usuario falla, se mantiene en la materia actual con una nueva pregunta aleatoria.
- **Meta:** El desafío concluye satisfactoriamente al completar un total de **10 preguntas**.
## 🛠️ Tecnologías y Librerías
- **Lenguaje:** Python 3.x
- **GUI:** `tkinter` (Interfaz nativa de Python).
- **Tratamiento de Imágenes:** `Pillow` (PIL) para la renderización de recursos visuales.
- **Base de Datos:** MySQL / MaríaDB.
## 📋 Instalación y Dependencias
Para ejecutar este proyecto, necesitas instalar las librerías necesarias:
```bash
# Instalación de Pillow para manejo de imágenes
pip install Pillow
# Instalación del conector de base de datos
pip install mysql-connector-python
```
## IMAGENES DEL EVENTO
<img width="330" height="300" alt="image" src="https://github.com/user-attachments/assets/7c61a118-f40f-428f-804c-1bb4a4b3ccf6" />
<img width="330" height="300" alt="image" src="https://github.com/user-attachments/assets/10c14562-1fb8-447f-be74-057591b9ac35" />
<img width="330" height="300" alt="image" src="https://github.com/user-attachments/assets/4b15b644-0dd2-4f6e-b553-1884cc0b6b46" />
<img width="400" height="310" alt="image" src="https://github.com/user-attachments/assets/82759620-1b67-4e14-ad56-4054bb750ce4" />

## 👥 Créditos y Colaboración
Este proyecto fue un esfuerzo colaborativo:
- **Derek Cerecedo García ([Derkpy](https://github.com/Derkpy))**: Desarrollo completo de la aplicación (Python), lógica de negocio, diseño de interfaz.
- **Luis Felipe Avila Cruz**: Diseño y arquitectura de la base de datos SQL.
---
*Desarrollado originalmente como parte de un proyecto universitario para la carrera de ISC del instituto tecnologico superior de escárcega.*


