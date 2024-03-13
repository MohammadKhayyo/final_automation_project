pipeline {
    agent any

    stages {
      stage('Set Python Env') {
            steps {
                bat '''
                    python3 -m venv venv
                    source venv/bin/activate
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
//                 sh 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Add test execution steps here
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