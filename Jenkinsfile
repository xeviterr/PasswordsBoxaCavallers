pipeline { 
    agent any 
    stages {
        stage('Build') { 
            steps { 
                sh 'python3 -m py_compile appTest.py ' 
            }
        }
        stage('Test'){
            steps {
                sh 'python3 appTest.py'
            }
        }
    }
}