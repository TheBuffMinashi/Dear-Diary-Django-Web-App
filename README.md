# Dear Diary - Django Web App

## Description:
Dear Diary is a web application built using Django that allows a single user to create and manage personal diaries.<br>
The users can create new entries, view and edit existing entries, and delete entries that are no longer needed.<br>
The app is built using Django templating language and uses MySQL as the database.<br>

## Installation
To install and run the application, follow these steps:

1. Clone the repository to your local machine:
<pre><code> git clone https://github.com/TheBuffMinashi/Dear-Diary-Django-Web-App.git </pre></code>

2. Install the required packages using pip:
<pre><code> pip install -r requirements.txt </pre></code>

3. Create a new MySQL database for the app.
4. Set up the database connection by adding the following information to the `DATABASES` setting in `settings.py`:
3. Run the migrations to create the necessary tables in the database:
<pre><code> python manage.py makemigrations </pre></code>
<pre><code> python manage.py migrate </pre></code>

