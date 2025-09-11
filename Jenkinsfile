pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ommi1987/uptime_kuma_link_onboaring.git',
                    credentialsId: 'uptime-kuma'
            }
        }
    }
}
