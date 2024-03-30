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
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_US --password-stdin'
            }
        }
        
       
        stage('Push App') {
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
