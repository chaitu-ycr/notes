## Jenkins examples

This folder contains ready-to-use `Jenkinsfile` examples you can copy into your repositories or point a Pipeline job at.

Files:
- `Jenkinsfile.nodejs` — simple Node.js CI (checkout, install, test, archive)
- `Jenkinsfile.docker` — uses a Docker image agent for reproducible environments
- `Jenkinsfile.matrix` — runs tests in parallel across multiple Node.js versions

- `Jenkinsfile.python` — Python CI example (pytest, artifact archive)
- `Jenkinsfile.cpp` — C++ CMake build + test example (Docker/gcc)

Usage:

1. Create a Pipeline job in Jenkins and select **Pipeline script from SCM**.
2. Point the job to your repository URL and set the **Script Path** to one of these files, e.g. `jenkins/examples/Jenkinsfile.nodejs`.
3. Save and click **Build Now**.

Local debugging tips:
- Use the same Docker image locally to reproduce build/container issues.
- If a job fails on Jenkins but not locally, verify environment variables, credentials, and node/tool versions.

Example Script Path values:
- `jenkins/examples/Jenkinsfile.nodejs`
- `jenkins/examples/Jenkinsfile.docker`
- `jenkins/examples/Jenkinsfile.matrix`

- `jenkins/examples/Jenkinsfile.python`
- `jenkins/examples/Jenkinsfile.cpp`

Want me to commit these into a branch and open a PR? Ask and I'll prepare the git commands for `pwsh.exe`.
