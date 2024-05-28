# todolist
Small application in Django
Prerequisites:
1. You have to install Docker
2. You need create files in ./env based on .env_example in current directory:



To run application you need execute these commands:
1. docker compose up

When you run application first time you have to create superuser as described below

2. docker ps
	- you need locate container ID with image "todo_project-app" and put it on instead of brackets i.e. y67u

3. docker exec -it [container ID - first 4 chars are enough] bash

4. python manage.py migrate

5. python manage.py createsuperuser 
You must give the name and password

6. exit

Now you can login to application with login and password as you set on address http://127.0.0.1:8080

