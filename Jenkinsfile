pipeline {
    agent any
    stages {
        stage("scan") {
            steps {
                sh 'sudo docker run --rm -v "${PWD}:/src" --workdir /src returntocorp/semgrep semgrep --config=auto --no-autofix'
            }
        }
    }
}
