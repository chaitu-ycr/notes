# 🏗️ Complete C++ Shared DLL Project with Conan & CMake

## Why Use This?
Build a C++ project that creates a shared DLL using Conan for dependency management and CMake for building—portable, reusable, and easy to automate!

---

## 1. Project Structure
```text
cpp_shared_dll_example/
├── CMakeLists.txt
├── src/
│   ├── mylib.cpp
│   └── mylib.h
├── app/
│   └── main.cpp
├── conanfile.py
```

---

## 2. Conan Recipe (`conanfile.py`)
```python
from conan import ConanFile
from conan.tools.cmake import CMake

class SharedDLLConan(ConanFile):
    name = "shared_dll_demo"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    requires = "fmt/10.1.1"
    exports_sources = "CMakeLists.txt", "src/*", "app/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

---

## 3. src/mylib.h
```cpp
#pragma once
#include <string>

#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT
#endif

DLL_EXPORT std::string get_greeting();
```

---

## 4. src/mylib.cpp
```cpp
#include "mylib.h"
#include <fmt/core.h>

std::string get_greeting() {
    return fmt::format("Hello from DLL!");
}
```

---

## 5. app/main.cpp
```cpp
#include "../src/mylib.h"
#include <iostream>

int main() {
    std::cout << get_greeting() << std::endl;
    return 0;
}
```

---

## 6. CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.15)
project(SharedDLLDemo)

find_package(fmt REQUIRED)

add_library(mylib SHARED src/mylib.cpp)
target_link_libraries(mylib PRIVATE fmt::fmt)

add_executable(app app/main.cpp)
target_link_libraries(app PRIVATE mylib)
```

---

## 7. Build & Run
```sh
conan install . --output-folder=build --build=missing
conan build . --build-folder=build
# Run the app (Windows)
build/app.exe
# Or (Linux/macOS)
./build/app
```
On Windows, make sure `mylib.dll` is in the same directory as `app.exe` or in your PATH.

---

## Troubleshooting & Tips
- If the app can't find the DLL, copy it to the executable directory or add its folder to your PATH.
- You can add more dependencies in `conanfile.py` as needed.
- Use `conanfile.py` and `conan build` for reproducible, automated builds.
- Use `conan create .` to package your DLL for reuse in other projects.
- For cross-platform DLL/shared library builds, check your compiler and linker settings in CMake.

---

💡 **Pro Tip:**
- Use Conan and CMake together for portable, automated DLL builds.
- Package your DLL with `conan create .` for easy reuse in other projects or teams!
