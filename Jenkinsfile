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
                    dockerapp = docker.build("flaskapp:latest", '-f Dockerfile .')
                }
            }
        }
        
       stage('Test') {
            steps {
                dir('app') {
                    sh 'pytest tests/ -v' 
                }
            }
        }
        
        stage('Run image') {
            steps {
                dir('app') {
                    sh 'python3 main.py' 
                }
            }
        }
           
    }
}
