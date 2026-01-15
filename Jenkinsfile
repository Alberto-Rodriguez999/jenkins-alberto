pipeline {
    agent any 

    stages {
        stage('1. Descargar Código') {
            steps {

                checkout scm 
            }
        }

        stage('2. Construir Imagen Docker') {
            steps {
                script {

                    sh 'docker build -t futbol-app:v1 .'
                }
            }
        }

        stage('3. Prueba de Existencia') {
            steps {
                script {

                    sh 'docker images | grep futbol-app'
                }
            }
        }
    }
    
    post {
        success {
            echo '¡Éxito! La aplicación se construyó correctamente.'
        }
        failure {
            echo 'Algo salió mal. Revisa los logs.'
        }
    }
}
