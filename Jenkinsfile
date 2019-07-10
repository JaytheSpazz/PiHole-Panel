pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
    }

    stages {
        stage('Build') {
            steps {
                sh 'debuild -us -uc pihole-panel/'
            }
        }
        
        stage('Cleanup'){
            steps {
                cleanWs deleteDirs: true, patterns: [[pattern: '*.deb', type: 'EXCLUDE']]
            }
        }
    }
}
