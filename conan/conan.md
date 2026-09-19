---
title: "Conan"
aliases:
  - "Conan"
---
## 🧰 Conan: Your Package Manager Sidekick

Ever tried building a C++ project and felt like you were assembling IKEA furniture with missing screws? That’s where **Conan** swoops in—like a superhero with a toolbox full of dependencies. And guess what? It’s not just for C++—Python folks, you get some love too!

### 🐍 Conan for Python Native Extensions

Conan is handy for packaging native extensions or managing C++ dependencies in Python projects.

#### 1. Install Conan (if you haven’t already)
```sh
pip install conan
```

#### 2. Create a Recipe for Your Extension
```sh
conan new mypyext/0.1 --template=header_only
```

#### 3. Add Build Requirements
Edit `conanfile.py`:
```python
tool_requires = "cmake/3.27.0"
```

#### 4. Build and Package
```sh
conan install . --output-folder=build --build=missing
conan build . --build-folder=build
```
The built extension or library will be in the `build` directory.

#### 5. Use in Your Python Project
You can call Conan from your build scripts or integrate with tools like `scikit-build` or `pybind11` for C++ extension modules.

⚠️ **Gotcha:** Conan doesn’t replace `pip`—it complements it for native code!

### 🐛 Debugging Story
Ever spent hours chasing a missing DLL or library? With Conan, just declare your dependency and let it fetch the right version. It’s like magic, but with fewer rabbits and more binaries.

Now go forth and build—minus the dependency drama! 🦸


