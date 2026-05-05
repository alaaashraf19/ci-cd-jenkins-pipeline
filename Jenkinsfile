pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
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