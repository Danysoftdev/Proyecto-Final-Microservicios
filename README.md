# 🧩 Microservicio de Gestión de Usuarios

Este proyecto es un microservicio desarrollado en **Python** que permite realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre una entidad de usuario, utilizando una base de datos **MySQL**. Está construido bajo principios de buenas prácticas de código, contenerización con **Docker**, y validación con **Pylint** y la guía de estilo **PEP8**.

## 🚀 Tecnologías utilizadas

- **Python 3**
- **MySQL**
- **Docker** & **Docker Compose**
- **Pylint** (análisis estático de código)
- **PEP8** (estándar de estilo en Python)
- **Flask** o FastAPI (según el framework que estés usando)
- **SQLAlchemy** (si aplica como ORM)

## 📁 Estructura del proyecto

```

📁 Proyecto-Final-Microservicios/
├── .github/workflows/                   # Workflows de GitHub Actions
├── FastAPI/
│ ├── app/
│ │ ├── alembic/                         # Migraciones de base de datos
│ │ ├── config/                          # Configuración del proyecto
│ │ ├── constants/                       # Constantes globales
│ │ ├── helpers/                         # Funciones utilitarias
│ │ ├── models/                          # Modelos ORM (SQLAlchemy)
│ │ ├── repositories/                    # Acceso a datos
│ │ ├── routes/                          # Endpoints de la API
│ │ ├── services/                        # Lógica de negocio
│ │ ├── .env / .env.example              # Variables de entorno
│ │ ├── alembic.ini                      # Configuración Alembic
│ │ └── main.py                          # Punto de entrada principal
│ ├── migrations.py
│ ├── Dockerfile
│ ├── requirements.txt
├── MySQL/
│ └── Dockerfile                         # Imagen personalizada de MySQL
├── docker-compose.yml                   # Orquestación de servicios
├── .dockerignore / .gitignore

````

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/Danysoftdev/Proyecto-Final-Microservicios.git
cd Proyecto-Final-Microservicios
````

2. **Construir y levantar los servicios con Docker**

```bash
docker-compose up --build
```

3. El microservicio estará disponible en `http://localhost:8080`

## 🧪 Validación de código

Para validar el código con **Pylint** y cumplir la guía **PEP8**, puedes ejecutar:

```bash
pylint app/
```

O si usas `flake8`:

```bash
flake8 app/
```

## 🛠️ Funcionalidades principales

* 📌 Crear un usuario
* 📄 Consultar todos los usuarios
* 🔍 Buscar usuario por ID o correo
* ✏️ Actualizar información del usuario
* ❌ Eliminar usuario

## 🧰 Requisitos

* Python 3.10+
* Docker y Docker Compose
* Editor como VSCode recomendado

## 📚 Licencia

Este proyecto es de uso académico y está licenciado bajo [MIT License](LICENSE).

---

### ✨ Autores

* **Nombres**: Daniela Villalba Torres y Alejandro Castaño Uzquiano
