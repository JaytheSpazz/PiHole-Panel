pipeline {
    agent any

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
