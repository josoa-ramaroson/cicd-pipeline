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
                            dockerImage = docker.build  registry + ":v1"
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
                sh "docker rmi $registry:v1"
            }
        }
        stage('Apply Kubernetes files') {
            steps {
                withKubeConfig([credentialsId: 'minikube-credentials', serverUrl: 'https://192.168.49.2:8443']) {
                    sh 'kubectl apply -f deployment '
                    
                    // sh "kubectl set image deployment/item-deployment items-container=${registry}:$BUILD_NUMBER"
                }

            }
        }
    }
}


