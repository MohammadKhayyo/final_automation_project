pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt' // Install dependencies if needed
                echo 'Building..'
            }
        }
         stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                sh 'python -m unittest Tests/test_api/test_runner.py' // Replace with your test command
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}