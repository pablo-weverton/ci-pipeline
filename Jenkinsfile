pipeline {
    agent any
    stages {
        stage('Build image') {
            steps {
                script {
                    dockerapp = docker.build("flaskapp:latest", '-f Dockerfile .')
                }
            }
        }
    }
}
