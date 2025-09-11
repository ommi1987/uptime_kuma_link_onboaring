pipeline {
    agent any

    environment {
        GIT_CRED = credentials('ef4fcb76-64f0-4cf0-af29-16e94c03fcd4')  // ID you saved in Jenkins
    }

    stages {
        stage('Run Python Script') {
            steps {
                sh '''
                # Pass Jenkins credentials as environment vars to Python
                export GITHUB_USER=$GIT_CRED_USR
                export GITHUB_PASS=$GIT_CRED_PSW
                python3 test2.py
                '''
            }
        }
    }
}
