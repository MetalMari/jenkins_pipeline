pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                git branch: "main",
                url: "https://github.com/MetalMari/jenkins_pipeline.git"
            }
        }
        stage("Pulling image from docker hub") {
            steps {
            sh """
            docker pull metalmari/codearena_mongo
            """
            }
        }
        stage("Tag new name") {
            steps {
            sh """
            docker tag metalmari/codearena_mongo:latest metalmari/mongo_db_codearena:latest
            """
            }
        }
        stage("Pushing image to dockerhub") {
            steps {
                withDockerRegistry(credentialsId: 'dockerhub-cred', url: 'https://index.docker.io/v1/') {
                sh """
                docker push metalmari/mongo_db_codearena:latest
                """
                }
            }
        }
    }
}