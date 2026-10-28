pipeline {
  agent any
  options { timestamps(); disableConcurrentBuilds() }
  environment {
    IMAGE_TAG = "${env.BUILD_NUMBER}-${env.GIT_COMMIT.take(7)}"
  }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Test') {
      steps {
        sh 'python3 -m pip install -r requirements-dev.txt'
        sh 'python3 -m pytest -q'
      }
    }
    stage('Filesystem Security Scan') {
      steps {
        sh 'trivy fs --scanners vuln,misconfig,secret --severity HIGH,CRITICAL --exit-code 1 .'
      }
    }
    stage('Build and Scan Images') {
      steps {
        script {
          ['user-service', 'product-service', 'order-service'].each { svc ->
            sh "docker build -t local/${svc}:${IMAGE_TAG} services/${svc}"
            sh "trivy image --severity HIGH,CRITICAL --exit-code 1 local/${svc}:${IMAGE_TAG}"
          }
        }
      }
    }
    stage('Publish') {
      when { branch 'main' }
      steps {
        echo 'Configure a protected registry credential and push step before enabling publishing.'
      }
    }
  }
  post {
    always { cleanWs(deleteDirs: true, notFailBuild: true) }
  }
}
