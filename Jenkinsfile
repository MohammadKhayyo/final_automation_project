pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat 'setx PATH "%PATH%;C:\\Python39\\Scripts"'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'python -m unittest Tests/test_api/test_runner.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}