# 📦 Using Prebuilt Binaries from Conan Center

## Why Use This?
Consume prebuilt binaries from Conan Center to speed up builds, avoid compiling dependencies, and simplify your workflow.

---

## 1. Add a Prebuilt Dependency (`conanfile.py`)
```python
from conan import ConanFile
from conan.tools.cmake import CMake

class ZlibDemoConan(ConanFile):
    name = "zlib_demo"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    requires = "zlib/1.2.13"
    exports_sources = "CMakeLists.txt", "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

---

## 2. Install & Build with Prebuilt Packages
```sh
conan install . --output-folder=build --build=missing
conan build . --build-folder=build
```
Conan will download prebuilt binaries for your platform and compiler if available.

---

## 3. Link in CMake
```cmake
find_package(ZLIB REQUIRED)
add_executable(myapp src/main.cpp)
target_link_libraries(myapp PRIVATE ZLIB::ZLIB)
```

---

## 4. Run the Built Binary
```sh
./build/myapp  # Or the correct binary name for your project
```

---

## Troubleshooting & Tips
- If Conan can't find a prebuilt binary for your platform, it will build from source automatically.
- You can swap out `zlib` for other libraries from Conan Center by changing the `requires` line in `conanfile.py`.
- Make sure your compiler and settings match those used for the prebuilt binaries.
- Use `conanfile.py` and `conan build` for reproducible, automated builds.

---

💡 **Pro Tip:**
- Prebuilt binaries save time and avoid toolchain headaches!
- Try other libraries from Conan Center—just update the `requires` line!