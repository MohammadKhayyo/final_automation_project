pipeline {
    agent any

    environment {
        PIP_PATH = 'C:\\Users\\Moham\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pip.exe'
        PYTHON_PATH = 'C:\\Users\\Moham\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {
//         stage('Setup Environment') {
//             steps {
//                 echo 'Setting up Python environment...'
// //                 bat "${PYTHON_PATH} -m venv venv"
// //                 bat "${PYTHON_PATH} -m pip install --upgrade pip"
//                 bat "${PIP_PATH} install -r requirements.txt"
//             }
//         }
        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setting up Selenium server HUB...'
                bat "start /B java -jar selenium-server.jar hub"
                // Delay for 10 seconds
                bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
            }
        }

        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setting up Selenium server nodes...'
                bat "start /B java -jar selenium-server.jar node --port 5555 --selenium-manager true"
                // Delay for 10 seconds
                bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
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
                bat "${PYTHON_PATH} -m unittest Tests/test_selenium/test_runner.py"
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
//             bat "rd /s /q venv"
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