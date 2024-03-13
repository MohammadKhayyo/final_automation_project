pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up virtual environment...'
                bat 'python -m venv venv' // Create a virtual environment named 'venv'
                bat 'venv\\Scripts\\activate' // Activate the virtual environment
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat 'venv\\Scripts\\pip install -r requirements.txt' // Install dependencies
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Include your build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here. Make sure to activate the virtual environment in each step where you need Python.
                bat 'venv\\Scripts\\activate && python -m unittest Tests/test_api/test_runner.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Include your deployment steps here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Add any post-build cleanup steps here
            // This could include deactivating the virtual environment, though it's typically not necessary in CI jobs as the environment is ephemeral
        }

        success {
            echo 'Build completed successfully.'
        }

        failure {
            echo 'Build failed.'
        }
    }
}
