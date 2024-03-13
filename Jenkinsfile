pipeline {
    agent any

    stages {
        stage ('Prepare Environment') {
            steps {
                // Assuming Python is in PATH; otherwise, use the full path to the python executable
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            source venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage ('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            source venv/bin/activate
                            python3 Tests/test_api/test_runner.py
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            python Tests/test_api/test_runner.py
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up virtual environment
                if (isUnix()) {
                    sh "rm -rf venv"
                } else {
                    bat "rd /s /q venv"
                }
            }
        }
    }
}
