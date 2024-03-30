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
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_US --password-stdin'
            }
        }
        
        stage('Push Database') {
            steps {
                sh 'docker push 3fastcoders/ca4_mongo:4.4.29-focal'
            }
        }


        // Member 2
        stage('Build') {
            steps {
                sh 'docker build -t 3fastcoders/ca5:latest .'
            }
        }

        stage('Push App') {
            steps {
                sh 'docker push 3fastcoders/ca5:latest'
            }
        }
        


        // Member 1
        stage('Check Docker Images Existence') {
            steps {
                script {
                    def frontendImage = sh(script: "docker image inspect analysts/3fastcoders/my-app", returnStatus: true) == 0
                    def backendImage = sh(script: "docker image inspect mongo:4.4.29-focal", returnStatus: true) == 0

                    if (frontendImage && backendImage) {
                        echo "Docker images found on Docker Hub"
                    } else {
                        error "Docker images not found on Docker Hub"
                    }
                }
            }
        }
        stage('Run Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }

    }
  
    post {
        always {
            sh 'docker logout'
        }
}
