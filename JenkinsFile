pipeline { 
    agent any 
    stages {
        stage('Build') { 
            steps { 
                sh 'python -m py_compile app.py ' 
            }
        }
        stage('Test'){
            steps {
                sh 'python app.py'
            }
        }
    }
}