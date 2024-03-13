pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up virtual environment...'
                // Make sure to replace the path with the actual path to your Python executable
                bat 'C:\\Python39\\python.exe -m venv venv'
                bat 'venv\\Scripts\\activate.bat'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                // Use the Python pip to install required packages from requirements.txt
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Include steps for your build process here
                // Example: bat 'build_command'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here, ensuring the virtual environment is activated
                // Note: The virtual environment's activation script for the current shell needs to be called in each command that requires it
                bat 'call venv\\Scripts\\activate.bat && python -m unittest Tests/test_api/test_runner.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Include steps for your deployment process here
                // Example: bat 'deploy_command'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Add any post-build cleanup steps here
            // Typically, deactivating the virtual environment isn't necessary in CI jobs, but you can add custom cleanup commands if needed
        }

        success {
            echo 'Build completed successfully.'
        }

        failure {
            echo 'Build failed.'
        }
    }
}
