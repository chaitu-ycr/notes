# 🛠️ Conan + CMake Example (C++)

## Why Use This?
Build a simple C++ project using Conan to manage dependencies and automate CMake builds—no more manual setup!

---

## 1. Project Structure
```text
cpp_cmake_example/
├── CMakeLists.txt
├── src/
│   └── main.cpp
├── conanfile.py
```

---

## 2. Conan Recipe (`conanfile.py`)
```python
from conan import ConanFile
from conan.tools.cmake import CMake

class DemoConan(ConanFile):
    name = "demo"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    requires = "fmt/10.1.1"
    exports_sources = "CMakeLists.txt", "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

---

## 3. CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.15)
project(ConanCMakeDemo)

find_package(fmt REQUIRED)

add_executable(demo src/main.cpp)
target_link_libraries(demo PRIVATE fmt::fmt)
```

---

## 4. src/main.cpp
```cpp
#include <fmt/core.h>

int main() {
    fmt::print("Hello, Conan + CMake!\n");
    return 0;
}
```

---

## 5. Build & Run
```sh
conan install . --output-folder=build --build=missing
conan build . --build-folder=build
./build/demo  # Or build/demo.exe on Windows
```

---

## Troubleshooting & Tips
- If you get errors about missing libraries, check your `requires` line in `conanfile.py`.
- You can swap out `fmt` for another library from Conan Center—just update the `requires` line!
- Use `conanfile.py` and `conan build` for reproducible, automated builds.

---

💡 **Pro Tips:**
- Try other libraries from Conan Center—dependency management is easy!
- Keep your build steps automated for fast, reliable development.
