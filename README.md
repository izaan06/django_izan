# Supermercado Django Project

## Introducción
Proyecto de gestión de supermercado con Django.

## Instalación
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`.
3. Ejecutar migraciones: `python manage.py migrate`.
4. Cargar datos iniciales: `python manage.py loaddata fixtures/initial_data.json`.

## Ejecución
`python manage.py runserver`  
Visitar http://127.0.0.1:8000/ para acceder.

## Tests
`python manage.py test`

## GitHub Actions
Archivo de CI en `.github/workflows/django-tests.yml`.
