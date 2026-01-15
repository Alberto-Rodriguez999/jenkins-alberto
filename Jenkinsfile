pipeline {
    agent any
    
    stages {
        stage('1. Descargar de GitHub') {
            steps {
                cleanWs()

                git branch: 'main', url: 'https://github.com/Alberto-Rodriguez999/jenkins-alberto.git'
            }
        }

        stage('2. Construir Imagen') {
            steps {

                sh 'docker build -t alberto-app .'
            }
        }

        stage('3. Test Automático') {
            steps {

                
                sh 'echo "4" | docker run -i --rm alberto-app'
            }
        }
    }
}
