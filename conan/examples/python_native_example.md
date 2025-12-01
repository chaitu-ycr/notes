# 🐍 Beginner's Guide: Python Extension Module with pybind11, Conan & CMake

## Why Use This?
Want to write fast C++ code and use it in Python? With pybind11, Conan, and CMake, you can build real Python modules in C++—no more dependency headaches!

---

## 1. Project Structure
```
python_cmake_integration/
├── conanfile.py
├── CMakeLists.txt
├── src/
│   └── mymodule.cpp
```

---

## 2. Conan Recipe (`conanfile.py`)
```python
from conan import ConanFile
from conan.tools.cmake import CMake

class PybindDemoConan(ConanFile):
    name = "pybind_demo"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    requires = "pybind11/2.10.4"
    exports_sources = "CMakeLists.txt", "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

---

## 3. Example Source File (`src/mymodule.cpp`)
```cpp
#include <pybind11/pybind11.h>
int some_function() { return 42; }
PYBIND11_MODULE(mymodule, m) {
    m.def("some_function", &some_function);
}
```

---

## 4. CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.15)
project(PyExtDemo)
find_package(pybind11 REQUIRED)
pybind11_add_module(mymodule src/mymodule.cpp)
```

---

## 5. Build Steps
Open a terminal in your project folder and run:
```sh
conan install . --output-folder=build --build=missing
conan build . --build-folder=build
```
The built module (e.g., `mymodule.pyd` or `mymodule.so`) will be in the `build` directory.

---

## 6. Use in Python
```python
import sys
sys.path.append("build")  # Ensure Python can find the built module
import mymodule
print(mymodule.some_function())
```

---

## 7. Troubleshooting & Common Gotchas
- Adjust module paths and extensions for your OS (Windows: `.pyd`, Linux: `.so`, macOS: `.dylib`).
- Make sure your Python path includes the build output directory (`sys.path.append("build")`).
- If you get import errors, check:
  - The module filename matches what you import (`mymodule`)
  - Your Python version matches the one used for building
  - The build output directory contains the compiled module
- If you see missing symbols or build errors, check your compiler and Python development headers are installed.

---

💡 **Pro Tips:**
- Use `conanfile.py` and `conan build` for reproducible, automated builds.
- pybind11 gives you a true Python module experience (with docstrings, exceptions, etc.).
- For more advanced bindings, see the [pybind11 docs](https://pybind11.readthedocs.io/en/stable/).
