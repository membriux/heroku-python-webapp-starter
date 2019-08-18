

# Python-Flask Web App Starter
This repo contains the necessary files to work on your next Python-Flask web application.

Feel free to **download/fork** it so you can use it as a reference!


## How to Deploy Flask-Python Web App on Heroku

### On your Terminal:

#### 1. Install virtual environment (in project directory):
- `cd my-project`
- `python3 -m venv venv`

![Install venv](gifs/walkthrough1.gif)


#### 2. Activate virtual environment for your project:
- `source venv/bin/activate`

![Activate venv](gifs/walkthrough2.gif)


#### 3. Install basic requirements for web app in Flask:
 - `pip install flask gunicorn`
 Note: make sure to have pip installed

![Install requirements](gifs/walkthrough3.gif)


#### 4. Verify requirements were installed with the desired versions:
- `pip freeze`

#### 5. Create requirements.txt so Heroku understands what your web app needs
- `pip freeze > requirements.txt`

![Create requirements.txt](gifs/walkthrough4.gif)


#### 6. Create Procfile (for Heroku):
- `vi Procfile`

On your Procfile file, type this:
- `web: gunicorn app:app`


![Create Procfile](gifs/walkthrough5.gif)



#### 7. Go to [Heroku Dashboard](http://heroku.com) -> sign in -> create app, and deploy using Github


![Deploy to Heroku](gifs/walkthrough6.gif)
