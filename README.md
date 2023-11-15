# crm_project

This is demo link of project
https://youtu.be/hDA1hKCSdeY


The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/sumit5529/crm_project.git
$ cd crm_project
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements
```

one thing more,you have to changes in database in setting file 
update the id and password of DB according you.


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd crm_project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

