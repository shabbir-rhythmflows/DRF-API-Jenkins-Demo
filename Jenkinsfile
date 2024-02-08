pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                echo "I INSTALL"
            }
        }
        stage('SonarQube Analysis') {
            steps {
            echo "ANALYSIS!"
            }
        }


        stage('Build Docker Image') {
            steps {
                echo 'BUILT SUCCESSFULLY'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "BUILD DOCKER IMAGE"
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