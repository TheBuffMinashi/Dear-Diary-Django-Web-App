# Dear Diary - Django Web App

## Description
Dear Diary is a web application built using Django that allows a single user to create and manage personal diaries.<br>
The users can create new entries, view and edit existing entries, and delete entries that are no longer needed.<br>
The app is built using Django templating language and uses MySQL as the database.<br>

## Installation Without Docker
To install and run the application, follow these steps:

1. Clone the repository to your local machine:
<pre><code>git clone https://github.com/TheBuffMinashi/Dear-Diary-Django-Web-App.git</pre></code>

2. Install the required packages using pip:
<pre><code>pip install -r requirements.txt</pre></code>

3. Create a new MySQL database for the app.
4. There is a file named `.env.sample` in the project's root directory. Change it's name to `.env` and complete the necessary variables:
```
SECRET_KEY = (Django secret key)
MYSQL_DATABASE = (name of the mysql database)
MYSQL_USER = (name of the mysql user)  
MYSQL_PASSWORD = (password for mysql user)
DB_PORT = (desired prt for mysql - default is 3306)
```
* You can generate a Django secret key from [this website](https://djecrety.ir/).

5. Run the migrations to create the necessary tables in the database:
<pre><code>python manage.py makemigrations</pre></code>
<pre><code>python manage.py migrate</pre></code>

6. Create a superuser for the app:
<pre><code>python manage.py createsuperuser</pre></code>

Follow the prompts to enter a username, email address, and password for the superuser.

7. Start the development server:
<pre><code>python manage.py runserver</pre></code>
If you want to run the app on a specific port, you can run:
<pre><code> python manage.py runserver 127.0.0.1:PORT NUMBER </pre></code>
replace `PORT NUMBER` with the desired port number.


## Installation With Docker
If you are not willing to install the dependencies on your system, you could easily build and run the project's docker container with 2 simple commands.

1. Clone the repository to your local machine:
<pre><code>git clone https://github.com/TheBuffMinashi/Dear-Diary-Django-Web-App.git</pre></code>
2. Before building the containers, You need to complete the `.env.sample` file and change it's name to `.env`:
```
SECRET_KEY = (Django secret key)
MYSQL_DATABASE = (name of the mysql database)
MYSQL_USER = (name of the mysql user)  
MYSQL_PASSWORD = (password for mysql user)
DB_PORT = (desired prt for mysql - default is 3306)
PORT = (desired port number)
MYSQL_ROOT_PASSWORD = (password for mysql root user)
```
3. Now you can build and run the containers:
```
docker-compose build
docker-compose up
```
You can access the application by heading to `localhost:PORT` in your browser. `PORT` is the same as the one in `.env` file.
## Usage
To use the application, follow these steps:

1. Log in with your superuser account.
2. Once logged in, you will be taken to the diary homepage where you can view all of your diary entries.
3. To create a new entry, click the "New Entry" button and fill out the form with your desired title and content.
4. To view an existing entry, click on the entry title in the diary homepage.
5. To delete or edit an entry, click on the entry title in the diary homepage and then click the "Delete" or "Edit" button.

## Next Steps
Here are some ideas for future improvements to this diary app:

* Add a page for your most recent entries.
* Give every weekday a color.
* Show the creation date in the HTML `<title>` tag.
* Create an emoji of the day selection for an entry.
* Paginate the list of entries.

Feel free to fork this project and implement any of these ideas or come up with your own. If you make any changes, please submit a pull request so that others can benefit from your improvements.

## Contributing
Contributions to this project are welcome! If you have any suggestions or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
This project was developed by Minashi, inspired by the tutorial [Build a Personal Diary With Django and Python](https://realpython.com/django-diary-project-python/) from Real Python. I would like to express my gratitude to the Django project for providing the powerful web framework that made this app possible.
