# CSV Analysis

This Django project allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations on a web interface.

## Features

- Upload CSV files
- Display the first few rows of the data
- Calculate summary statistics (mean, median, standard deviation) for numerical columns
- Identify, display and handle missing values
- Generate basic plots (histograms) for numerical columns

## Setup Instructions

### Prerequisites

- Python 3.6+
- Django 3.2+
- pandas
- numpy
- matplotlib
- seaborn

### Installation

1. Clone the repository:

```sh
git https://github.com/krishnalath99/VE3-Assignment-CSV-Analysis.git
cd VE3-Assignment-CSV-Analysis
```

2. Create a virtual environment and activate it:

```sh
virtualenv name_of_venv
name_of_venv/Scripts/activate
```

3. Install the Dependencies

```sh
pip install django
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
```

4. Apply migrations:

```sh
python manage.py migrate
```

5. Run the development server:

```sh
python manage.py runserver
```

6. Open your web browser and go to http://127.0.0.1:8000/csv-analysis/ to use the application.
