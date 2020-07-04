pipeline { 
    agent any 
    stages {
        stage('Build') { 
            steps { 
                sh 'python3 -m py_compile app.py ' 
            }
        }
        stage('Test'){
            steps {
                sh 'python3 app.py'
            }
        }
    }
}