pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'C:\\Python39\\python.exe -m venv venv' // Create a virtual environment
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt' // Use pip from venv
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                // Other build steps
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'venv\\Scripts\\python.exe -m unittest Tests/test_api/test_runner.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Deployment steps
            }
        }
    }
}
