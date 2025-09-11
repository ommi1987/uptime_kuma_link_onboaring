pipeline {
    agent any

    environment {
        GIT_CRED = credentials('ef4fcb76-64f0-4cf0-af29-16e94c03fcd4')  // ID you saved in Jenkins
    }

    parameters {
        string(name: 'ISP_NAME', defaultValue: '', description: 'Mandatory! Enter in format: WH_NAME-LOCATION-ISP_NAME-TYPE-BW (e.g. 7STAR-Mumbai-Hathway-BB-100)')
        string(name: 'ISP_PUBLIC_IP', defaultValue: '', description: 'Mandatory! Enter ISP Public IP (e.g. 1.2.3.4)')
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
        withCredentials([usernamePassword(credentialsId: 'ef4fcb76-64f0-4cf0-af29-16e94c03fcd4',
                                          usernameVariable: 'GITHUB_USER',
                                          passwordVariable: 'GITHUB_PASS')]) {
            sh """
                . venv/bin/activate
                python test2.py "${ISP_NAME}" "${ISP_PUBLIC_IP}" 
                    
            """
                }
            }
        }
    }
}
