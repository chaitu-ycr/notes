## Jenkins examples

This folder contains ready-to-use `Jenkinsfile` examples you can copy into your repositories or point a Pipeline job at.

Files:

**Basic Pipelines:**
- `nodejs_pipeline.jenkinsfile` — Node.js CI (checkout, install, test, archive)
- `python_pipeline.jenkinsfile` — Python CI example (pytest, artifact archive)
- `cpp_pipeline.jenkinsfile` — C++ CMake build + test example (Docker/gcc)

**Advanced Features:**
- `docker_build_pipeline.jenkinsfile` — Uses a Docker image agent for reproducible environments
- `matrix_build_pipeline.jenkinsfile` — Runs tests in parallel across multiple Node.js versions
- `scheduled_pipeline.jenkinsfile` — Cron trigger example for nightly builds
- `input_parameters_pipeline.jenkinsfile` — Build with user-defined parameters
- `deployment_pipeline.jenkinsfile` — Deployment pipeline with manual approval gate
- `shared_library_pipeline.jenkinsfile` — Example of using a shared library

Usage:

1. Create a Pipeline job in Jenkins and select **Pipeline script from SCM**.
2. Point the job to your repository URL and set the **Script Path** to one of these files, e.g. `jenkins/examples/nodejs_pipeline.jenkinsfile`.
3. Save and click **Build Now**.

Local debugging tips:
- Use the same Docker image locally to reproduce build/container issues.
- If a job fails on Jenkins but not locally, verify environment variables, credentials, and node/tool versions.
