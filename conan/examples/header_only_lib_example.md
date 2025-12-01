# 📚 Header-Only Library Example with Conan

## Why Use This?
Package and use a header-only C++ library with Conan for easy reuse, sharing, and reproducible builds—no compilation required!

---

## 1. Create Recipe (`conanfile.py`)
```python
from conan import ConanFile

class MyHeaderLibConan(ConanFile):
    name = "myheaderlib"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    exports_sources = "include/*"

    def package(self):
        self.copy("*.h", dst="include", src="include")

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
```

---

## 2. Add Your Header(s)
Place your header file(s) in the `include/` folder. Example: `include/myheader.h`

---

## 3. Build & Test Locally
```sh
conan install . --output-folder=build --build=missing
conan build . --build-folder=build
```
No compilation step is needed for header-only libraries, but this ensures packaging and integration work.

---

## 4. Use in Another Project
Add to your project's `conanfile.py`:
```python
requires = "myheaderlib/0.1"
```
Or in CMake:
```cmake
find_package(myheaderlib REQUIRED)
target_include_directories(myapp PRIVATE ${myheaderlib_INCLUDE_DIRS})
```

---

## Troubleshooting & Tips
- Make sure your headers are in the correct `include/` folder.
- If your library uses templates, all code must be in the headers.
- Header-only libraries are super portable and easy to share!
- Use `conanfile.py` and `conan build` for reproducible, automated builds.

---

💡 **Pro Tip:**
- You can publish your header-only library to Conan Center or share privately for instant reuse!