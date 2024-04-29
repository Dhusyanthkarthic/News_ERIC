How to Run the Application:
Clone the Repository: 
git clone <repository-url>
Install Dependencies: 
cd <repository-directory>
pip install -r requirements.txt

Set Up Environment Variables: If the application requires any environment variables (e.g., API keys, database credentials), set them up either by exporting them in your shell or by creating a .env file.

Run the Application: Start the Flask application using the following command:
python app.py

Access the Application: Once the application is running, you can access it in your web browser by navigating to http://localhost:5000.

How the Workflows Work:
CI/CD Pipeline Trigger: The CI/CD pipeline is triggered automatically whenever there is a new commit or push to the main branch of the repository.

Build Job:
The pipeline starts with a build job that runs on an Ubuntu environment.
It checks out the code, installs dependencies, and runs unit tests to ensure code quality.

Deployment Job:
If the build job succeeds, the pipeline triggers the deployment job.
The deployment job deploys the application to the specified cloud service (e.g., Heroku) using the provided API key.
If the deployment is successful, the application is updated and made available for users to access.
