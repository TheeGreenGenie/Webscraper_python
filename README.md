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

git clone https://github.com/TheeGreenGenie/Webscraper_python.git
cd Webscraper_python


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