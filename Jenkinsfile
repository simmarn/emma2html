pipeline {
  agent {
    node {
      label 'windows_10_pro_n_vs2017'
    }

  }
  stages {
    stage('Build container') {
      steps {
        bat 'docker build -t simmarn/emma2html:win -f docker-windows/Dockerfile .'
      }
    }
    stage('Push container') {
      steps {
        bat 'docker login -u simmarn -p banankola && docker push simmarn/emma2html:win'
      }
    }
  }
}