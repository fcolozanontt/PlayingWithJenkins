pipeline {
    agent any
    stages {
        stage('Check Version') {
            steps{
                sh 'python --version'
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python main.py'
            }
        }
        stage('Wrapping it up') {
            steps {
                echo 'We are done here'
            }
        }
    }
}