pipeline {
    agent any
    
    tools {
        // Corrección 1: Usamos el nombre compatible con tu versión de Jenkins
        'hudson.plugins.sonar.SonarRunnerInstallation' 'SonarScanner'
    }
    
    stages {
        stage('1. Descargar Código') {
            steps {
                cleanWs()
                // TUS DATOS: Tu repositorio real
                git branch: 'main', url: 'https://github.com/Alberto-Rodriguez999/jenkins-alberto.git'
            }
        }

        stage('2. Análisis de Calidad (SonarQube)') {
            steps {
                script {
                    // Corrección 2: Definimos la ruta exacta para evitar el error "not found"
                    def scannerHome = tool name: 'SonarScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    
                    withSonarQubeEnv('SonarServer') {
                        // TUS DATOS: He puesto 'tarea3' (lo que vi en tu foto).
                        // Si en SonarQube le pusiste otro nombre al proyecto, cámbialo aquí.
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=tarea3 -Dsonar.sources=."
                    }
                }
            }
        }

        stage('3. Construir Docker') {
            steps {
                // TUS DATOS: Tu nombre de imagen (le añadí :sonar para diferenciarla)
                sh 'docker build -t alberto-app:sonar .'
            }
        }

        stage('4. Test Automático') {
            steps {
                // TUS DATOS: Tu truco del "4" y tu imagen
                sh 'echo "4" | docker run -i --rm alberto-app:sonar'
            }
        }
    }
}
