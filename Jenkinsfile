pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3-alpine'
                    args '-v gi'
                }
            }
            steps {
                sh 'python3 pihole-panel/main.py' 
            }
        }
    }
}
