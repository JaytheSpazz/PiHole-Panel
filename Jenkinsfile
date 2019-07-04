pipeline {
    agent {
        docker { image 'ubuntu:latest' }
    }
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
    }

    stages {
        stage('Build') {
            steps {
                sh 'cd ${WORKSPACE}/Pihole-Panel'
                sh 'dpkg --build Pihole-Panel/ PiHole-Panel-latest.deb'
            }
        }
        
        stage('Cleanup'){
            steps {
                cleanWs deleteDirs: true, patterns: [[pattern: '*.deb', type: 'EXCLUDE']]
            }
        }
    }
}
