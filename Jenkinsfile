pipeline{
    agent any
    
    stages {
        stage('checkout code'){
            steps {
                checkout scm

            }
        }
          stage('setup python'){
            steps {
                sh "python3 -m  pip install -r requirments.txt"
            }
        }
        stage('run python program'){
            steps {
                sh "python3 extract.py"
            }
        }
    }
}