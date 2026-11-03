Grade Calculator
Description
Grade Calculator is a Python application that calculates students' averages and determines whether they pass or fail. It also classifies averages into grade categories.
Installation
Clone the repository and install the required dependencies:
pip install -r requirements.txt
Usage
Use the calculator functions to calculate a student's average, check whether the student passes, and determine the grade category:
calculate_average(grades) – Calculates the average of grades.
is_passing(average) – Returns whether the average is at least 10.
get_grade_category(average) – Returns one of four categories:
Excellent: average >= 16
Good: average >= 12 and below 16
Average: average >= 10 and below 12
Fail: average below 10
Run Tests
Execute the unit tests using:
pytest -v
Run Linting
Check code quality using:
flake8 .