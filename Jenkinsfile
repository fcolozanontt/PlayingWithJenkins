pipeline {
    agent any
    stages {
        stage('Check Version') {
            steps{
                bat '$python --version'
            }
        }
        stage('Run Python Script') {
            steps {
                bat '$python main.py'
            }
        }
        stage('Wrapping it up') {
            steps {
                echo 'We are done here'
            }
        }
    }
}