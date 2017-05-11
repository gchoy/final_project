# Review and Rate a Physical Therapist

A simple review and rate app created with Django and Python.

## Demo

You can find the app hosted on [python anywhere](http://gchoy.pythonanywhere.com/reviews/welcome/).

## Installing and running locally

1. Install [PostgreSQL](https://www.postgresql.org/).
2. Create a [virtual env](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/).
3. Activate the virtual env.
4. Use ```pip install``` to install the dependencies listed below within the virtual environment:

```
Django==1.11
django-bootstrap3==8.2.3
django-filter==1.0.2
django-registration-redux==1.6
django-widget-tweaks==1.4.1
nose==1.3.7
numpy==1.12.1
pandas==0.19.2
Pillow==4.1.1
psycopg2==2.7.1
python-dateutil==2.6.0
scikit-learn==0.18.1
scipy==0.19.0
sympy==1.0
Werkzeug==0.12.1
```
5. Clone the repo.
6. Once everything is installed run ```python manage.py runserver```.

## User Stories

* This is an app where users can rate and comment on Physical Therapists that belong to a medical institution.
* The user will be able to obtain personalized suggestions about Physical Therapists.
* The user will be able to search the Physical Therapist database based on name, last name and/or keywords

## Built With

* [PostgreSQL](https://www.postgresql.org/)
* [Django](https://www.djangoproject.com/) - One of many Web frameworks for Python
* [Python](https://www.python.org/)


## Author

**Gabriela Choy**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* All the GA TA's and Instructors.
