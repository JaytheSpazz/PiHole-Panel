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
                sh 'apt-get update'
                sh 'apt-get install python-stdeb fakeroot python-all'
                sh '''        
                python setup.py --command-packages=stdeb.command bdist_deb\\;
                '''
            }
        }
        
        stage('Cleanup'){
            steps {
                cleanWs deleteDirs: true, patterns: [[pattern: '*.deb', type: 'EXCLUDE']]
            }
        }
    }
}
