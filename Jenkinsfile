pipeline {
    agent any

    environment {
        PIP_PATH = 'C:\\Users\\Moham\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pip.exe'
        PYTHON_PATH = 'C:\\Users\\Moham\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
//                 bat "${PYTHON_PATH} -m venv venv"
//                 bat "${PYTHON_PATH} -m pip install --upgrade pip"
                bat "${PIP_PATH} install -r requirements.txt"
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Your build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                bat "${PYTHON_PATH} -m unittest Tests/test_api/test_runner.py"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Your deployment steps here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "rd /s /q venv"
        }

        success {
            echo 'Build succeeded.'
            // Additional steps for successful build
        }

        failure {
            echo 'Build failed.'
            // Additional steps for failed build
        }
    }
}
