# CONFIGURACION INICIAL
## Instalar dependencias
```bash
$ python -m venv ~/.envs/curso_edteam_drf
$ source ~/.envs/curso_edteam_drf/bin/activate
$ pip install -r requeriments.txt
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```
## DJANGO ADMIN
### Creación de super usuario
```bash
$ ./manage.py createsuperuser
Username (leave blank to use 'minombre'):
Email address: micorreo@midominio.com
Password:MiClave123
Password (again):MiClave123
Superuser created successfully.
```
