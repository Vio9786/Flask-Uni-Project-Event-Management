Rose Website


This project is a Flask-based W.O.Z (WIZARD OF OZ) web application designed for an event planning company to assist with cervical screening-related decision support using an AI prediction model. Users can log in as either an administrator or employee to import data, generate predictions, and view screening outcome pages.

The system is organized using a modular Flask structure, featuring clean templates, static assets, form handling, and route management.



Key Features:

Wizard of Oz AI Prediction Model
   Processes cervical screening input data and provides outcome predictions.

Role-Based Login System

Modular Flask Architecture
   Routes, forms, configuration, and templates separated for clarity.

Static Asset Management
   Icons, branding images, and UI graphics stored in /app/static.

User-Friendly Templates
   HTML pages (index, login, prediction, import, outcome, revision, etc.) built with Jinja2.



Login Credentials:
Use the following credentials to access the system:

Admin Account
Username: Admin1
Password: 123

Employee Account
Username: Employee1
Password: 123



System Structure:

RoseWebsite/
│
├── app/
│   ├── __pycache__/
│   ├── static/
│   │   ├── BackArrowIcon.png
│   │   ├── LanguageIcon.png
│   │   ├── LogoutIcon.png
│   │   ├── ROSE-Foundation.png
│   │   └── ROSE-FoundationLoginImage.png
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── import.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── outcome.html
│   │   ├── prediction.html
│   │   └── revision.html
│   │
│   ├── __init__.py
│   ├── forms.py
│   └── routes.py
│
├── venv/
│
├── config.py
├── RoseWebsite.py
├── Developer Modules.py
└── requirements.txt


###############################################
IMPORTANT

Ensure that you are in the RoseWebsite Directory

Ensure that you have python version 3.11 or later installed and have an appropriate interperitor selected
###############################################

How to Run:
1:
	cd RoseWebsite
2:
	python -m venv venv	
3:

	source venv/bin/activate      # macOS / Linux
	venv\Scripts\activate         # Windows
4:
	pip install -r requirements.txt
5: 
	flask run


Important Notes:

Virtual environment activation is required each time before launching the app.

Credentials provided are for demonstration only—change them before deploying to any production environment.


