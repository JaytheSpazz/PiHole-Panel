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
                /*
                    Sign and upload from workstation since instance is not online 24/7
                    and would require storing GPG key in an unsecure manner.

                sh 'dput ppa:daleosm/pihole-panel pihole-panel_2.3_source.changes'
                */
            }
        }
        
        stage('Cleanup'){
            steps {
                /*
                    We need the output files since we are building on workstation.
                
                cleanWs deleteDirs: true, patterns: [[pattern: '*.deb', type: 'EXCLUDE']]
                */
            }
        }
    }
}
