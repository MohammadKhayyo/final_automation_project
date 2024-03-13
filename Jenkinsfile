pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Replace 'C:\\Python39\\Scripts\\' with the actual path to the pip executable on your Jenkins agent.
                bat 'C:\\Python39\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Replace 'C:\\Python39\\python.exe' with the actual path to the Python executable on your Jenkins agent.
                bat 'C:\\Python39\\python.exe -m unittest Tests/test_api/test_runner.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Deployment steps go here
            }
        }
    }
}
