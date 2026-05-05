pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('install dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') { //creates a report of each unit test
            steps {
                bat 'python run_tests.py'
            }
        }
    }
    post{ //parses the reports of our test results
        always{
            junit 'test_results.xml'
        }
    }
}