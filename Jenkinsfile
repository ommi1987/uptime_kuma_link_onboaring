pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ommi1987/uptime_kuma_link_onboaring.git',
                    credentialsId: 'ef4fcb76-64f0-4cf0-af29-16e94c03fcd4'
            }
        }
    }
}
