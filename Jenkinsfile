pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '3', artifactNumToKeepStr: '30'))
    }

    stages {
        stage('Build') {
            steps {
                sh 'dpkg-deb --build ${WORKSPACE}/Pihole-Panel PiHole-Panel-latest.deb'
            }
        }
        
        stage('Cleanup'){
            steps {
                cleanWs deleteDirs: true, patterns: [[pattern: '*.deb', type: 'EXCLUDE']]
            }
        }
    }
}
