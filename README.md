# Todo App

A simple task management application built with Django.

## Features

- Create, read, update, and delete tasks
- Mark tasks as complete
- Organize tasks by categories

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```
5. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

- `Tasks/`: The main application for task management
- `todo_project/`: Project configuration files
- `templates/`: HTML templates for the project
- `static/`: Static files (CSS, JavaScript, images)

## Technologies Used

- Django
- SQLite
- Bootstrap (if used)
- Django Widget Tweaks

## License

This project is licensed under the MIT License - see the LICENSE file for details.