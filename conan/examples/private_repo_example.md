# 🔒 Using Private Conan Repositories (Artifactory, etc.)

## Why Use This?
Fetch packages from a private Conan server (like Artifactory) securely, using `conanfile.py` and reproducible build steps. Great for company-internal dependencies!

---

## 1. Add Your Private Remote
```sh
conan remote add myremote https://mycompany.jfrog.io/artifactory/api/conan/conan-local
```
You only need to add the remote once per machine.

---

## 2. Authenticate Securely
```sh
# Use environment variables or CI secrets for credentials
conan remote login myremote $CONAN_USER --password $CONAN_PASSWORD
```
In CI, set `$CONAN_USER` and `$CONAN_PASSWORD` as secrets or environment variables.

---

## 3. Install & Build from Private Repo
```sh
conan install . --remote=myremote --output-folder=build --build=missing
conan build . --build-folder=build
```
This will fetch dependencies from your private server and build your project.

---

## 4. Run the Built Binary
```sh
./build/myapp  # Or the correct binary name for your project
```

---

## 5. Example `conanfile.py`
```python
from conan import ConanFile
from conan.tools.cmake import CMake

class PrivateDemoConan(ConanFile):
    name = "private_demo"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    requires = "myprivatepkg/1.0@mycompany/stable"
    exports_sources = "CMakeLists.txt", "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

---

## Troubleshooting & Best Practices
- Don’t commit your credentials! Always use environment variables or CI secrets.
- If you get authentication errors, check your username/password and remote URL.
- For CI/CD, use `conan remote login` in your pipeline before running install/build.
- Use `conanfile.py` and `conan build` for reproducible, automated builds from private repos.

---

💡 **Pro Tip:**
Keep your remote and credentials out of source control. Use profiles and environment variables for maximum security and reproducibility!
