# pybind11 Guide

`pybind11` is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code. Its goals and syntax are similar to the excellent Boost.Python library by David Abrahams: to minimize boilerplate code in traditional extension modules by inferring type information using compile-time introspection.

## Why pybind11?

- **Lightweight**: Header-only, no external dependencies (unlike Boost.Python).
- **Modern C++**: Built for C++11 and newer.
- **Seamless Integration**: Easy to use with CMake.
- **Powerful**: Supports functions, classes, exceptions, STL containers, numpy arrays, and more.

## Prerequisites

Before you begin, ensure you have:

- A C++ compiler (GCC, Clang, MSVC) supporting C++11 or later.
- Python (3.6+ recommended) and `pip`.
- CMake (3.4+ recommended).

## Installation

### 1. Using pip (for Python-only projects or testing)
You can install pybind11 as a Python package, which is useful for headers and CMake config files.
```bash
pip install pybind11
```

### 2. As a Git Submodule (Recommended for C++ projects)
If you are maintaining a C++ repository, adding pybind11 as a submodule is often the best approach.
```bash
git submodule add https://github.com/pybind/pybind11.git extern/pybind11
git submodule update --init
```

## First Steps: Binding a Simple Function

Let's create a simple C++ function and expose it to Python.

### C++ Code (`example.cpp`)

```cpp
#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function that adds two numbers");
}
```

- `PYBIND11_MODULE(example, m)`: This macro creates the entry point. `example` is the module name (must match the filename of the shared object), and `m` is the variable used to define bindings.
- `m.def`: Exposes a function. You can provide docstrings as the third argument.

## Building the Module

The modern way to build C++ Python extensions is using **CMake** combined with **pyproject.toml** (via `scikit-build-core`).

### 1. CMakeLists.txt

Create a `CMakeLists.txt` to define your C++ build:

```cmake
cmake_minimum_required(VERSION 3.15)
project(example)

find_package(pybind11 REQUIRED)

pybind11_add_module(example example.cpp)
```

### 2. pyproject.toml

Create a `pyproject.toml` to define the Python package and build system:

```toml
[build-system]
requires = ["scikit-build-core", "pybind11"]
build-backend = "scikit_build_core.build"

[project]
name = "example"
version = "0.0.1"
```

### 3. Build and Install

You can now build and install the package using standard Python tools:

```bash
pip install .
```

This will:
1.  Read `pyproject.toml`.
2.  Install build dependencies (`scikit-build-core`, `pybind11`).
3.  Run CMake to configure and build the extension.
4.  Install the resulting package.

## Testing the Module

Once built, you can import it in Python:

```python
import example

print(example.add(1, 2))  # Output: 3
print(example.add.__doc__) # Output: A function that adds two numbers
```

## Binding Classes

Binding classes is just as intuitive.

### C++ Code

```cpp
struct Pet {
    Pet(const std::string &name) : name(name) { }
    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }

    std::string name;
};

PYBIND11_MODULE(example, m) {
    py::class_<Pet>(m, "Pet")
        .def(py::init<const std::string &>())
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName)
        .def_readwrite("name", &Pet::name);
}
```

- `py::class_<Pet>(m, "Pet")`: Defines a Python class named `Pet`.
- `.def(py::init<...>())`: Exposes the constructor.
- `.def_readwrite`: Exposes a public member variable directly.

### Python Usage

```python
import example

p = example.Pet("Molly")
print(p.getName())  # Molly
p.setName("Charly")
print(p.name)       # Charly
```

## STL Containers

pybind11 can automatically convert STL containers like `std::vector` and `std::map` to Python lists and dicts. You just need to include the header.

```cpp
#include <pybind11/stl.h>

std::vector<int> get_range(int n) {
    std::vector<int> result;
    for (int i = 0; i < n; ++i)
        result.push_back(i);
    return result;
}

// In PYBIND11_MODULE:
// m.def("get_range", &get_range);
```

Python side:
```python
print(example.get_range(5)) # [0, 1, 2, 3, 4]
```

## Recommended Project Structure

For a hybrid C++/Python project:

```text
my_project/
├── CMakeLists.txt
├── extern/
│   └── pybind11/
├── src/
│   ├── main.cpp
│   └── bindings.cpp
├── python/
│   └── test_example.py
├── pyproject.toml
```

This setup allows you to build the C++ core independently or install the whole package as a Python library.
