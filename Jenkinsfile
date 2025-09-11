pipeline {
    agent any
    parameters {
        string(name: 'NAME', defaultValue: 'Omprakash', description: 'Enter name')
        string(name: 'AGE', defaultValue: '25', description: 'Enter age')
    }
    stages {
        stage('Run Python') {
            steps {
                sh """
                python3 test1.py ${params.NAME} ${params.AGE}
                """
            }
        }
    }
}
