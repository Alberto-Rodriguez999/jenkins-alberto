pipeline {
    agent any
    
    stages {
        stage('1. Descargar Código') {
            steps {
                cleanWs()
                // Descarga el código de GitHub
                git branch: 'main', url: 'https://github.com/Alberto-Rodriguez999/jenkins-alberto.git'
            }
        }

        stage('2. Construir Docker') {
            steps {
                // Crea la imagen
                sh 'docker build -t alberto-app .'
            }
        }

        stage('3. Test Automático') {
            steps {
                // Ejecuta la app y le pasa un "4" para que no se quede colgada
                sh 'echo "4" | docker run -i --rm alberto-app'
            }
        }
    }
}
