pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
    }

    stages {
        stage('Build') {
            steps {
                dir("pihole-panel") {
                    sh "debuild -us -uc"
                }
            }
        }
    }
}
