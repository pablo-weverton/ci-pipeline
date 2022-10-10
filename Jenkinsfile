pipeline {
    agent any
    stages {
        stage('Checkout git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '691db04d-0236-484b-ab3d-32070af3ce9f', url: 'https://github.com/pablo-weverton/ci-pipeline.git']]])
            }
        }
        stage('Build image') {
            steps {
                script {
                    dockerapp = docker.build("flaskapp:latest", '-f Dockerfile .')
                }
            }
        }
    }
}
