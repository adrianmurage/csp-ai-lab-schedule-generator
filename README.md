# USIU Lab Schedule Generator

## Description
The USIU Lab Schedule Generator is a Flask web application designed to automate the assignment of labs to classes in a university course schedule. It takes a CSV file containing course schedule data as input, processes the data to assign labs to classes, and generates a lab schedule that can be viewed on the web.

## Features

1. Upload CSV file: Users can upload a CSV file containing the course schedule data.
Generate Lab Schedule: The application processes the uploaded data to assign labs to classes and generates a lab schedule.
1. View Schedule: Users can view the generated lab schedule on the web interface.
1. Error Handling: The application provides informative error messages and handles various edge cases gracefully.

## Assumptions

- All labs can handle the capacity of all courses.
- If the classes assigned to a specific time exceed the number of labs available, it will cause an error.
- No collisions occur in the class schedule provided.


## Setup

1. Clone the repository: `git clone git@github.com:adrianmurage/csp-ai-lab-schedule-generator.git`
1. Navigate to the project directory: `cd csp-ai-lab-schedule-generator`
1. Create a virtual environment: `python3 -m venv venv`
1. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Run the application: `python3 api/index.py`
1. Access the application in your web browser at `http://localhost:5000`

## Usage

1. Optionally download the sample course schedule or generate your own copy following the advised CSV format.
2. Upload the CSV file containing the course schedule data.
3. View the generated lab schedule on the web interface.
