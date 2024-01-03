# Your Project Name

This is a simple Django project for user registration, login, and profile functionality.

## Setup

### 1. Create a Virtual Environment

```bash
# On Unix or MacOS
python3 -m venv venv

# On Windows
python -m venv venv

# On Unix or MacOS
source venv/bin/activate

# On Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
