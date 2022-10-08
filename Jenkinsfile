pipeline {
    agent any
    stages {
        stage('Checkout git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '2eec7b60-71c2-4ecc-a0c8-42612e8287da', url: 'https://github.com/pablo-weverton/ci-pipeline.git']]])
            }
        }
        stage('Build image') {
            steps {
                script {
                    docker = docker.build("flaskapp:latest", '-f Dockerfile .')
                }
            }
        }
    }
}