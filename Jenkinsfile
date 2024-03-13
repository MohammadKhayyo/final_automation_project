pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''
                    python -m venv venv
                    venv\\Scripts\\activate.bat
                '''
            }
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