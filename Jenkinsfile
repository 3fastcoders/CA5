pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('3fastcoders-dockerhub')
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t 3fastcoders/my-app:latest .'
            }
        }
        
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                echo 'Login Completed'
                
            }
        }
        
        stage('Push') {
            steps {
                sh 'docker push 3fastcoders/my-app:latest'
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
        }
    }
}
