pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                git branch: "main",
                url: "https://github.com/MetalMari/docker-compose_jenkins.git"
            }
        }
        stage("Up containers with docker-compose") {
            steps {
            sh """
            docker-compose up -d
            """
            sh """
            docker ps
            """
            }
        }
        stage("Tag new name") {
            steps {
            sh """
            docker images
            """
            sh """
            docker tag mariadb:10.1 metalmari/mariadb:latest
            """
            sh """
            docker tag php:7.2.1-apache metalmari/php:latest
            """
            }
        }
        stage("Pushing new images") {
            steps {
                withDockerRegistry(credentialsId: 'dockerhub-cred', url: 'https://index.docker.io/v1/') {
                sh """
                docker push metalmari/mariadb:latest
                """
                sh """
                docker push metalmari/php:latest
                """
                }
            }
        }
        stage("Stop containers") {
            steps {
            sh """
            docker-compose down
            """
            sh """
            docker ps -a
            """
            }
        }
    }
}