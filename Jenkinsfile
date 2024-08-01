pipeline {
    environment {
        registry = "josoa/itemapi"
        registryCredential = "dockerhub_id"
        dockerImage = ''
    }
    agent any 
    stages{
        
        stage('checkout source') {
            steps{
                git branch: 'main', url:"https://github.com/josoa-ramaroson/cicd-pipeline.git"
            }
        }

        stage('Build images') {
                    steps{
                        script {
                            dockerImage = docker.build  registry + ":$BUILD_NUMBER"
                        }
                        }
                }
        
        stage('Push to registry') {
                    steps{
                        script {
                            docker.withRegistry('', registryCredential) {
                                dockerImage.push()
                            }
                        }
                    }
                }
        
            
        stage('Cleaning up'){
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
        stage('Apply Kubernetes files') {
            withKubeConfig([credentialsId: 'user1', serverUrl: 'https://api.k8s.my-company.com']) {
                sh 'kubectl apply -f deployment'
            }
        }
    }
}