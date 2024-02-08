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
        // stage('SonarQube Analysis') {
        //     steps {
        //         withSonarQubeEnv(sonarserver) {
        //             script {
        //                 withSonarQubeEnv(credentialsId: 'demodjangoshabbirtoken') {
        //                     sh "${scannerHome}/bin/sonar-scanner"
        //                 }
        //             }
        //         }
        //     }
        // }


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
                script {
                    withCredentials([usernamePassword(credentialsId: 'ubuntuServer', passwordVariable: 'REMOTE_PASSWORD', usernameVariable: 'REMOTE_USER')]) {
                        remote = [:]
                        remote.name = 'ubuntu test server'
                        remote.host = env.REMOTE_USER
                        remote.user = 'root'
                        remote.password = env.REMOTE_PASSWORD
                        remote.allowAnyHosts = true

                        stopExitStatus = sh(script: 'docker stop django-demo', returnStatus: true)

                        if (stopExitStatus == 0) {
                            sshCommand remote: remote, command: 'echo "CONTAINER Exists! Deleting it!"'
                            // Container exists, stop and remove it
                            // sshCommand remote: remote, command: 'docker stop reconciliation-demo'
                            sshCommand remote: remote, command: 'docker rm django-demo'
                        }
                        if (stopExitStatus == 1) {
                            sh 'echo "Did not delete container as it did not exist"'
                        }

                        sshCommand remote: remote, command: "docker run -d --name django-demo -p 8084:8000 shabbirhythm/demo-django-books:\\$env.BUILD_ID"
                    }
                }
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