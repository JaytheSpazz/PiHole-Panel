pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'dpkg-deb --build ${WORKSPACE}/Pihole-Panel PiHole-Panel-latest.deb'
            }
        }
        
        stage('Cleanup'){
            cleanWs deleteDirs: true, patterns: [[pattern: '*', type: 'INCLUDE'], [pattern: '.deb', type: 'EXCLUDE']]
        }
    }
}
