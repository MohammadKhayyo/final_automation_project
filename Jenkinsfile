pipeline {
    agent any

    environment {
        // Define any environment variables if needed
        // PYTHON_PATH = "C:/path/to/python.exe" // Uncomment and set the correct path if needed
    }

    stages {
        stage('Checkout') {
            steps {
                // Assuming Git SCM is correctly configured
                checkout scm
                echo 'Checked out the repository.'
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Add build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                script {
                    try {
                        // If PYTHON_PATH is set, use that, otherwise just 'python'
                        // bat "${env.PYTHON_PATH} hello.py" // Uncomment if using PYTHON_PATH
                        bat 'python hello.py' // Use this line if 'python' command is in PATH
                    } catch (Exception e) {
                        echo "Failed to run hello.py: ${e.getMessage()}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Add deployment steps here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Add any post-build cleanup steps here
        }

        success {
            echo 'Build completed successfully.'
        }

        failure {
            echo 'Build failed.'
        }
    }
}
