
How to setup and Deploy a project to Heroku steps

Install virtual environment (in project directory):
- python3 -m venv venv

Activate virtual environment:
- source venv/bin/activate

Install basic requirements for web app in Flask:
 - pip install flask gunicorn

Verify files:
- pip freeze

Create requirements.txt
- pip freeze > requirements.txt

Create Procfile (for Heroku):
- vi Procfile

Procfile contents:
- web: gunicorn app:app

Go to Heroku.com, create app, and deploy using Github
