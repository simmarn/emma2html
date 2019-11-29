node("windows_10_pro_n_vs2017") {

    checkout scm

    def app

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("simmarn/emma2html:win -f docker-windows/Dockerfile")
    }

    stage('Push image') {
        /* Finally, we'll push the image
         * Pushing multiple tags is cheap, as all the layers are reused. */
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push()
        }
    }
}