pipeline{
    agent any 

    environment {
        IMAGE= "dkhan573/flask-cicd-demo"
        EC2_HOST= "54.163.212.39" }

stages{
    stage('checkout'){
        steps{
            git branch: 'master'
            url: 'https://github.com/danish573/Flask-cicd-demo.git'
        }
    }
    stage('Build Docker Image'){
        steps{
            script{
                sh "docker build -t ${IMAGE}:${BUILD_NUMBER}"
                sh "docker tag ${IMAGE}:${BUILD_NUMBER} ${IMAGE}:latest"
            }
        }
    }
    stage('Push to DockerHub'){
        steps{
            withCredentials([usernamePassword(credentialsId:'dockerhub-creds',
                                              usernameVariable:'DOCKER_USER'
                                              passwordVariable: 'DOCKER_PASS')]){
                sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
            }
            sh "docker push ${IMAGE}:${BUILD_NUMBER}"
            sh "docker push ${IMAGE}:latest"
        }
    }
    stage('DEploy on EC2'){
        steps{
            sshagent (credentials: ['ec2-ssh-key']){
                sh """
                ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} '
                        docker pull ${IMAGE}:${BUILD_NUMBER} &&
                        docker stop flaskapp || true &&
                        docker rm flaskapp || true &&
                        docker run -d --name flaskapp -p 80:5000 ${IMAGE}:${BUILD_NUMBER}
                    '
                """
            }
        }
    }
}

post{
    always{
        cleanWs()
        }
    }

}

