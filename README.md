# Django Web Scraper

A modern Django application that extracts metadata and images from websites. This tool allows users to analyze websites and download images with a sleek, responsive interface.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/)
- **Git**: Download from [git-scm.com](https://git-scm.com/downloads)
- **pip**: Usually included with Python installation

### Cloning the Repository

1. Open your terminal or command prompt
2. Clone the repository to your local machine:

git clone https://github.com/yourusername/django-web-scraper.git
cd django-web-scraper


### Setting Up a Virtual Environment

Creating a virtual environment keeps your project dependencies isolated from other Python projects.

#### Windows:

# Create a virtual environment
python -m venv webscrapervenv

# Activate the virtual environment
webscrapervenv\Scripts\activate

#### macOS/Linux:

# Create a virtual environment
python3 -m venv webscrapervenv

# Activate the virtual environment
source webscrapervenv/bin/activate

You'll know the virtual environment is active when you see `(webscrapervenv)` at the beginning of your command line.

### Installing Dependencies

Once your virtual environment is active, install the required packages:

pip install -r requirements.txt

If the requirements.txt file doesn't exist or you want to create a fresh one, install the necessary packages individually:

pip install django==5.2
pip install requests
pip install beautifulsoup4
pip install python-dotenv
pip install gunicorn

### Database Setup

Set up the database with the following commands:

# Create the database tables based on your models
python manage.py makemigrations scraper

# Apply the migrations
python manage.py migrate

### Creating a Superuser (Optional)

If you want to access the admin panel, create a superuser account:

python manage.py createsuperuser

Follow the prompts to set up your username, email, and password.

### Running the Server

Start the development server:

python manage.py runserver

The application will be available at http://127.0.0.1:8000/

## Using the Web Scraper

1. Open your browser and navigate to http://127.0.0.1:8000/
2. Enter a website URL in the input field (with or without http/https prefix)
3. Click "Scrape Website" to start the analysis
4. View the extracted metadata and images on the results page
5. Download individual images or all images as a ZIP archive

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

deactivate

## Troubleshooting

### Common Issues and Solutions

#### Missing Modules
If you encounter a "ModuleNotFoundError", make sure:
- Your virtual environment is activated
- You've installed all required dependencies
- You're running commands from the project root directory

#### Database Migrations Errors
If you see migration errors:

python manage.py migrate --run-syncdb

#### Permission Issues (Linux/macOS)
If you encounter permission errors:

chmod +x manage.py

#### SSL Certificate Issues
For SSL certificate errors when scraping websites:

pip install certifi

## Deployment Tips

When you're ready to deploy the application:

1. Update `settings.py`:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Set up a production database

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Consider using:
   - Gunicorn or uWSGI as the application server
   - Nginx or Apache as the web server
   - PostgreSQL as the database

## Contributing

If you'd like to contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request