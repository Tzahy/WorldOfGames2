pipeline {
agent any
    stages {
        stage('checkout repo from github') {
            steps {
                git 'https://github.com/Tzahy/WorldOfGames2.git'
            }
        }
        stage('build image and run container') {
            steps {
                sh 'docker-compose up'
            }
        }
    }
}
