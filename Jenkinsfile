pipeline {
    agent any

    stages {
        stage('Diagnostic') {
        steps {
            bat 'echo %PATH%'
            bat 'dir C:\\Python39\\Scripts'
            // Use the above outputs to debug the issue further
        }
    }
        stage('Build') {
            steps {
                echo 'Building..'
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