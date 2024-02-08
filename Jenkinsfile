pipeline {
    agent any
    environment {
        dockerHome = tool 'rhythmDocker'
        PATH = "$dockerHome/bin::$PATH"
        scannerHome = tool 'sonarqubescanner'
        sonarserver = 'sonarserver'
    }
    stages {
        // stage('Install') {
        //     steps {
        //         echo "I INSTALL"
        //     }
        // }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv(sonarserver) {
                    script {
                        withSonarQubeEnv(credentialsId: 'demodjangoshabbirtoken') {
                            sh "${scannerHome}/bin/sonar-scanner"
                        }
                    }
                }
            }
        }


        stage('Build Docker Image') {
            steps {
                script {
                    imageName = "shabbirhythm/demo-django-books:${env.BUILD_ID}"
                    docker.build(imageName)
                }
                echo 'BUILT SUCCESSFULLY'
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        docker.image("shabbirhythm/demo-django-books:${env.BUILD_ID}").push()
                    }
                }
                echo "PUSHED SUCCESSFULLY"
            }
        }
        stage('Deploy With SSH') {
            steps {
                echo "PUSHED DOCKER IMAGE "
            }
        }

}
    post {
        success {
            echo 'DjangoRF API DEMO Pipeline executed successfully'
        }
        failure {
            echo 'DjangoRF API DEMO Pipeline Pipeline execution failed'
        }
        changed {
            echo 'Status of build changed!'
        }
    }
}