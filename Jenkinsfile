pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run API Test') {
            steps {
                bat "docker run --name api_test_runner ${IMAGE_NAME}:${TAG} python Tests/test_api/test_runner.py"
                bat "docker rm api_test_runner"
            }
        }

        stage('Run UI Test') {
            steps {
                bat "docker run --name ui_test_runner ${IMAGE_NAME}:${TAG} python Tests/test_selenium/test_runner.py"
                bat "docker rm ui_test_runner"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}