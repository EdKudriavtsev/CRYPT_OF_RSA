start http://127.0.0.1:8000/
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
start http://127.0.0.1:8000/