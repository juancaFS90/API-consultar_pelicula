# 🎬 API Consultar Película

API REST desarrollada en Python que permite consultar información de películas.
La aplicación está contenerizada con Docker para facilitar su despliegue y ejecución en cualquier entorno.

---

## 🛠 Tecnologías

- Python 3.x
- FastAPI
- Uvicorn
- Docker
- Docker Compose

---

## ⚙ Instalación Local (Sin Docker)

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/API-consultar_pelicula.git
cd API-consultar_pelicula
```
## 🐍 Crear Entorno Virtual

Crear el entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## ✅ 2️⃣ Instalación de dependencias

## 📦 Instalación de Dependencias

Una vez activado el entorno virtual, instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```
---

## ✅ 3️⃣ Ejecutar con Docker Compose

## 🐳 Ejecutar con Docker Compose

Si el proyecto incluye un archivo `docker-compose.yml`, ejecutar:

```bash
docker compose up --build
```
---

## ✅ 4️⃣ Endpoints
## 📌 Endpoints

### 🔎 Obtener película por nombre

GET /pelicula/{nombre}

Ejemplo:

GET http://localhost:8000/pelicula/inception

Ejemplo de respuesta:

```json
{
  "titulo": "Inception",
  "año": "2010",
  "director": "Christopher Nolan",
  "genero": "Sci-Fi",
  "rating": "8.8"
}
```
