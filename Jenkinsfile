pipeline {
    agent any
    stages {
        stage("scan") {
            steps {
                sh 'docker run --rm -v "${PWD}:/src" returntocorp/semgrep semgrep'
            }
        }
    }
}