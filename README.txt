Hello Follow the instructions 

#####################################
first Clone the git in cmd
---------------------------
git clone https://github.com/RedHaider/techforing_backend_project_django.git
cd techforing_project

######################################
then create virtual environment 
-------------------------------
python -m venv venv
source venv/bin/activate

3#####################################

install the requirements.txt to install dependencies 
----------------------------------------------------
pip install -r requirements.txt

######################################
Apply database migrations:
-------------------------
python manage.py makemigrations
python manage.py migrate
######################################
Run the server
--------------
python manage.py runserver

######################################

