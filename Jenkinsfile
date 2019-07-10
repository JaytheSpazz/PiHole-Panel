pipeline {
    agent any
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
    }

    stages {
        stage('Build') {
            steps {
                sh 'cd ${WORKSPACE}/pihole-panel'
                sh 'debuild -S -sa'
                /*
                    Sign and upload from workstation since instance is not online 24/7
                    and would require storing GPG key in an unsecure manner.

                sh 'dput ppa:daleosm/pihole-panel pihole-panel_2.3_source.changes'
                */
            }
        }
        
        stage('Cleanup'){
            steps {
                cleanWs deleteDirs: true, patterns: [[pattern: '*.deb', type: 'EXCLUDE']]
            }
        }
    }
}
