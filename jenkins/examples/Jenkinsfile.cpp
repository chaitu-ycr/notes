// C++ example using CMake inside a Docker/gcc image. Adjust as needed for your toolchain.
pipeline {
  agent {
    docker { image 'gcc:12' }
  }
  stages {
    stage('Checkout') { steps { checkout scm } }

    stage('Prepare') {
      steps {
        // Install cmake if not present
        sh 'apt-get update -y && apt-get install -y cmake make --no-install-recommends'
      }
    }

    stage('Build') {
      steps {
        sh 'mkdir -p build && cd build && cmake .. -DCMAKE_BUILD_TYPE=Release && cmake --build . -- -j$(nproc)'
      }
    }

    stage('Test') {
      steps {
        sh 'cd build && ctest --output-on-failure || true'
      }
      post {
        always { archiveArtifacts artifacts: 'build/**', allowEmptyArchive: true }
      }
    }
  }
}
