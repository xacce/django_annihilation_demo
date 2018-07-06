# django_annihilation_demo
Convert anything to django orm example
```
git clone https://github.com/xacce/django_annihilation_demo
cd django_annihilation_demo
pip install django==1.11
pip install -e git+https://github.com/xacce/django_annihilation.git#egg=django_annihilation
pip install -e git+https://github.com/xacce/annihilation.git#egg=annihilation
./manage.py migrate
./manage.py annihilate annihilation_django_demo/habr.yaml
./manage.py annihilate annihilation_django_demo/reddit.yaml
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8000
```
