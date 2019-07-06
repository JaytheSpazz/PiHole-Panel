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
                sh 'apt update'
                sh 'apt install build-dep -y fdupes'

                sh 'cd ${WORKSPACE}/Pihole-Panel'
                sh 'debuild -S -sa'
                sh 'dput ppa:daleosm/pihole-panel pihole-panel_2.3_source.changes'
            }
        }
        
        stage('Cleanup'){
            steps {
                cleanWs deleteDirs: true, patterns: [[pattern: '*.deb', type: 'EXCLUDE']]
            }
        }
    }
}
