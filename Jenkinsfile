pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                  python3 -m venv venv
                  source venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh '''
                      source venv/bin/activate
                      python test2.py --user $USER --password $PASS
                    '''
                }
            }
        }
    }
}

