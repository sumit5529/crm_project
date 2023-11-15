# crm_project

This is demo link of project
https://youtu.be/hDA1hKCSdeY
# Table of Contents
+ [About](#description)
+ [Authentication](#auth)
+  [Chat_Screen](#chat)
+ [Technologies Used](#built_with)
+ [Getting Started](#getting_started)


## About <a name="description"></a>
+ Displayed a list of customers with basic information (name, email, phone) in a table format. 
+ Provideded a form for users to add new customers. Fields include name, email, phone, address, and GST No.
+ Allowed users to edit customer details and save the changes.
+ Implemented a delete button for each customer record to allow users to delete a customer from the database.
### Authentication <a name="auth"></a>
+ Implemented a user authentication system where users can register with their email and password.
+ Upon registration, sent a verification email to the user's email address with a verification link. Once the user verifies the email, they can log in to the application.

### Chat_Screen<a name="chat"></a>
+ When a user clicks on a chat icon, displayed a communication history screen showing past interactions. Included timestamp, type of communication, and conversation details.
+ Included a button to send an email to the selected customer. Fetch the customer's email from the database and allowed the user to compose and sent emails directly from the CRM application.
 

## Technologies Used <a name="built_with"></a>
Website:
+ HTML
+ CSS 
+ JS
+ Django
+ Python
+ SQL

## Getting Started <a name="getting_started"></a>
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

