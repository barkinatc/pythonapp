pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "barkinatici/kubernetes"  // Docker image adı
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Kodun GitHub’dan çekilmesi
                git branch: 'master', url: 'https://github.com/barkinatc/pythonapp'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Docker image oluşturulması
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Deploy MongoDB') {
            steps {
                // MongoDB Deployment’ı çalıştırma
                sh 'kubectl apply -f mongodb-deployment.yaml'
               

                // MongoDB’nin Running olmasını bekleme
                script {
                    def status = ""
                    def retries = 10
                    while (retries > 0) {
                        status = sh(script: "kubectl get pods -l app=mongodb -o jsonpath='{.items[0].status.phase}'", returnStdout: true).trim()
                        if (status == "Running") {
                            echo "MongoDB pod is running."
                            break
                        }
                        echo "Waiting for MongoDB to be ready..."
                        sleep(10)
                        retries--
                    }
                    if (status != "Running") {
                        error("MongoDB pod did not reach Running state. Exiting pipeline.")
                    }
                }
            }
        }

        stage('Deploy Python App') {
            steps {
                // Python uygulamasını çalıştırma
                sh 'kubectl apply -f python-app-deployment.yaml'
                
            }
        }
    }

    post {
        always {
            echo 'Pipeline çalıştırıldı.'
        }
        success {
            echo 'Pipeline başarıyla tamamlandı.'
        }
        failure {
            echo 'Pipeline başarısız oldu.'
        }
    }
}
