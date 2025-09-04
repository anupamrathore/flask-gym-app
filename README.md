**Flask Gym App**

A simple Flask application for managing gym-related operations.


**Running the Application Locally**

*Prerequisites*: 

1. Python 3.9+
2. pip
3. Docker


**Clone the repository**

              *bash 
               git clone https://github.com/<your-username>/flask-gym-app.git
               cd flask-gym-app


**Set up a virtual environment (optional but recommended)**

              *bash 
               python -m venv venv
               source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**Install dependencies**

             *bash
              pip install -r requirements.txt


**Run the app**

             *bash
              python app.py
              The app should now be running at: http://localhost:5000


**Running Tests Locally**

             *bash
              pytest -v tests/




**🐳 Running the Application with Docker**

*Prerequisites*

1. Docker Desktop installed and running


            *Build the Docker Image*
              Bash -  docker build -t flask-gym-app .

            *Run the Container*
              Bash - docker run -p 5000:5000 flask-gym-app


             *Visit: http://localhost:5000*

💡 Note: When prompted to allow Docker access to private/public networks, allow both, especially if testing on a browser.

✅ Running Tests Locally

You can run all unit tests using Pytest:

pytest -v tests/



**GitHub Actions CI/CD Pipeline**

This project includes a GitHub Actions workflow that:

1. Triggers on every push or pull request to the main branch.
2. Sets up Python 3.9 environment on Ubuntu.
3. Installs dependencies from requirements.txt.
4. Runs unit tests using pytest.
5. You can find the workflow in .github/workflows/main.yaml.

