pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Use the confirmed paths here
                bat 'C:\\ConfirmedPathToPython\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Use the confirmed path to the python executable here
                bat 'C:\\ConfirmedPathToPython\\python.exe -m unittest Tests/test_api/test_runner.py'
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
