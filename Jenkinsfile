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
				sh 'docker-compose up -d'
            }
        }
		stage('run test') {
            steps {
				sh 'python tests/e2e.py'
            }
        }
	}
	catchError {
		sh 'docker stop jenkinspipelinewithgithub_project_1'
		sh 'docker rmi -f jenkinspipelinewithgithub_project_1'
	}
}


	