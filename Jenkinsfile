pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Assuming Python is installed in 'C:\Python39'
                bat 'C:\\Python39\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Assuming the 'python' command is available in 'C:\Python39'
                bat 'C:\\Python39\\python.exe -m unittest Tests/test_api/test_runner.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Add deployment steps here
            }
        }
    }
}
