pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('3fastcoders-dockerhub')
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t 3fastcoders/ca5:latest .'
            }
        }
        
        stage('Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: '3fastcoders-dockerhub', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh "echo ${DOCKERHUB_PASSWORD} | docker login -u ${DOCKERHUB_USERNAME} --password-stdin"
                }
            }
        }
        
        stage('Push') {
            steps {
                sh 'docker push 3fastcoders/ca5:latest'
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
        }
    }
}

