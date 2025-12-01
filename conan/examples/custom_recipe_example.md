# 🍳 Custom Conan Recipe Example

## Why Use This?
Create and share your own C++ library as a Conan package using `conanfile.py` for reproducible builds and easy reuse across projects and teams.

---

## 1. Create Recipe (`conanfile.py`)
```python
from conan import ConanFile
from conan.tools.cmake import CMake

class MyLibConan(ConanFile):
    name = "mylib"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    exports_sources = "CMakeLists.txt", "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

---

## 2. Add Your Sources
Place your source files in the `src/` folder and update `CMakeLists.txt` as needed for your library.

---

## 3. Build & Test Locally
```sh
conan install . --output-folder=build --build=missing
conan build . --build-folder=build
```
This ensures your recipe works before sharing.

---

## 4. Export & Share Your Package
Export your package to the local cache:
```sh
conan export .
```
Upload to a remote server (e.g., Artifactory):
```sh
conan upload mylib/0.1@ --remote=myremote
```
Make sure you have added and authenticated to your remote first.

---

## Troubleshooting & Tips
- If upload fails, check your remote URL and authentication.
- Use semantic versioning for your packages (`0.1.0`, `1.0.0`, etc.).
- Custom recipes make your code reusable across projects and teams.
- Use `conanfile.py` and `conan build` for reproducible, automated builds.

---

💡 **Pro Tip:**
- You can share your package privately or publish to Conan Center for global reuse!
