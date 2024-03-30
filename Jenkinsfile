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
                script {
                    // Extract username and password from credentials
                    def creds = credentials('3fastcoders-dockerhub')
                    def username = creds?.username ?: ''
                    def password = creds?.password ?: ''
                    sh "echo ${password} | docker login -u ${username} --password-stdin"
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
