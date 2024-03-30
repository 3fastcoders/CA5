pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('3fastcoders-dockerhub')
    }
    
    stages {

        // Member 3
        stage('Pull') {
            steps {
                sh 'docker pull mongo:4.4.29-focal'
            }
        }
        
        stage('Tag') {
            steps {
                sh 'docker tag mongo:4.4.29-focal 3fastcoders/ca4_mongo:4.4.29-focal'
            }
        }
        
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        
        stage('Push') {
            steps {
                sh 'docker push 3fastcoders/ca4_mongo:4.4.29-focal'
            }
        }
       
    }

     post {
        always {
            sh 'docker logout'
        }
     }
  
}
