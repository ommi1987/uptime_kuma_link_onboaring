pipeline {
    agent any

    environment {
        GIT_CRED = credentials('ef4fcb76-64f0-4cf0-af29-16e94c03fcd4')  // ID you saved in Jenkins
    }

    parameters {
        string(name: 'ISP_NAME', defaultValue: 'WH_NAME-LOCATION-ISP_NAME-TYPE-BW', description: 'EX: 7 STAR-Mumbai-Hathway-BB-100')
        string(name: 'ISP_PUBLIC_IP', defaultValue: 'NONE', description: 'ENTER ISP PUBLIC IP')
    }

    stages {
        stage('Install Dependencies') {
    steps {
        sh '''
        python3 -m venv venv
        . venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        '''
        }
    }

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
