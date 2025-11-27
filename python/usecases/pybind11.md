# pybind11: What, Why, and How

**pybind11** is a lightweight, header-only library that enables seamless interoperability between C++ and Python. It allows you to expose C++ classes, functions, and data structures to Python, making it easy to call C++ code from Python scripts and vice versa.

---

## 🎯 pybind11: Practical, Tricky, and Fun Usages

```cpp
// ===== 1. Install pybind11 =====
// pip install pybind11
// Or add as a submodule in your C++ project

// ===== 2. Expose a Simple Function =====
#include <pybind11/pybind11.h>
namespace py = pybind11;
int add(int i, int j) { return i + j; }
PYBIND11_MODULE(example, m) {
    m.def("add", &add, "A function that adds two numbers");
}
// Python:
// import example
// print(example.add(2, 3))

// ===== 3. Expose a C++ Class =====
#include <pybind11/pybind11.h>
namespace py = pybind11;
class Pet {
public:
    Pet(const std::string &name) : name(name) {}
    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }
private:
    std::string name;
};
PYBIND11_MODULE(example, m) {
    py::class_<Pet>(m, "Pet")
        .def(py::init<const std::string &>())
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName);
}
// Python:
// dog = example.Pet("Fido")
// print(dog.getName())
// dog.setName("Rex")
// print(dog.getName())

// ===== 4. Wrap C++ Library for Python =====
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
namespace py = pybind11;
py::array_t<uint8_t> process_image(py::array_t<uint8_t> input) {
    // ... call C++ code to process image ...
}
PYBIND11_MODULE(imgproc, m) {
    m.def("process_image", &process_image);
}
// Python:
// import imgproc
// imgproc.process_image(...)

// ===== 5. Fun: STL Containers and NumPy Arrays =====
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
// Expose std::vector, std::map, and NumPy arrays easily

// ===== 6. Pro-Tips =====
// Use PYBIND11_MODULE for module definition
// Use .def for functions and methods
// Use .def_property for properties
// Use pybind11::array for NumPy interoperability
// Use CMake or setuptools for building
```
