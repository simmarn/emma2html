pipeline {
  agent {
    label 'windows_10_pro_n_vs2017'
  }
    stages {

        stage('Build image') {
            /* This builds the actual image; synonymous to
            * docker build on the command line */
            steps {

                app = docker.build("simmarn/emma2html:win -f docker-windows/Dockerfile .")
            }
        }

        stage('Push image') {
            /* Finally, we'll push the image with two tags:
            * First, the incremental build number from Jenkins
            * Second, the 'win' tag.
            * Pushing multiple tags is cheap, as all the layers are reused. */
            steps {
                docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                    app.push("${env.BUILD_NUMBER}")
                    app.push("win")
                }
            }
        }
    }
}