
# Employee Management System

This is a simple **Employee Management System** built using Django (Function-Based Views). It allows users to perform basic CRUD operations (Create, Read, Update, Delete) for managing employees. 

## Features

- Add new employees
- View the list of employees
- Update employee details
- Delete employees
- User authentication (Login and Logout)

## Project Structure

```
Employee-Management-System/
├── EmployeeCRUD/
│   ├── fbvcrudproject/          # Django project directory
│   ├── static/css/              # CSS stylesheets
│   │   └── style.css            # Styling for the application
│   ├── templates/testapp/       # HTML templates
│   │   ├── base.html            # Base template for other pages
│   │   ├── index.html           # Employee list page
│   │   ├── insert.html          # Add new employee page
│   │   ├── update.html          # Update employee page
│   │   └── employee_detail.html # View employee details
│   ├── testapp/                 # Application directory
│   │   ├── models.py            # Database models
│   │   ├── views.py             # Views for handling requests
│   │   ├── forms.py             # Forms for employee data
│   │   └── urls.py              # Application-specific URLs
│   ├── db.sqlite3               # SQLite database
│   ├── manage.py                # Django management script
│   └── populate.py              # Script to populate the database with sample data
```

## Prerequisites

- Python 3.8+
- Django 4.x
- Bootstrap (included via CDN)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shreyash0019/Employee-Management-System.git
   cd Employee-Management-System/EmployeeCRUD
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
