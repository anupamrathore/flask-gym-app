**Flask Gym App**

A simple Flask application for managing gym-related operations.


**Running the Application Locally**

*Prerequisites*: 

1. Python 3.9+
2. pip
3. Docker


**Clone the repository**

              *bash - git clone https://github.com/<your-username>/flask-gym-app.git*
              *bash - cd flask-gym-app*


**Set up a virtual environment (optional but recommended)**

             *bash - python -m venv venv*
             *bash - source venv/bin/activate  # On Windows use `venv\Scripts\activate`*

**Install dependencies**

             *bash - pip install -r requirements.txt*


**Run the app**

             *bash - python app.py*
             The app should now be running at: http://localhost:5000


**Running Tests Locally**

             *bash - pytest -v tests/*






**GitHub Actions CI/CD Pipeline**

This project includes a GitHub Actions workflow that:

1. Triggers on every push or pull request to the main branch.
2. Sets up Python 3.9 environment on Ubuntu.
3. Installs dependencies from requirements.txt.
4. Runs unit tests using pytest.
5. You can find the workflow in .github/workflows/main.yaml.

