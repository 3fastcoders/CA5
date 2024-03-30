pipeline {
    agent any

    stages {
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
}
