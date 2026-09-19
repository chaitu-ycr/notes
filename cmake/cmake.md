---
title: "CMake"
aliases:
  - "CMake"
---
# 🚀 CMake: Taming the C++ Build Beast

Let's be honest: building C++ can feel like a dark art. You chant `g++ -I... -L... -l...`, sacrifice a rubber chicken, and hope for the best. If it works on your machine, you pray it works on your teammate's.

Enter CMake. It's not a build system. It's the *boss* of build systems. You give it one set of simple instructions (`CMakeLists.txt`), and it generates the right spells for any platform (Makefiles, Visual Studio projects, etc.). Think of it as your long-suffering, hyper-competent project manager.

This guide will turn you from a CMake-hater into a CMake-appreciator. Maybe even a fan. (Okay, let's not get carried away.)

## 🔗 Related topics

- [Conan](../conan/conan.md) — dependency management and package reproducibility paired with CMake
- [GitHub Actions](../github_actions/github_actions.md) — CI jobs often build C/C++ projects via CMake
- [Jenkins](../jenkins/jenkins.md) — self-hosted build pipelines commonly use CMake in automation jobs
- [Integration](../integration/integration.md) — the delivery and tooling layer where CMake is used in practice
- [Testing](../testing/testing.md) — build and validation flows depend on reliable CMake-driven projects

## 🚀 Level 1: Your First "Hello, CMake" Project

Let's start with the absolute basics.

### Step 1: Project Structure

```bash
mkdir hello_cmake
cd hello_cmake
touch main.cpp CMakeLists.txt
```

### Step 2: The Code (`main.cpp`)

The simplest C++ program imaginable.

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, CMake!" << std::endl;
    return 0;
}
```

### Step 3: The Magic Recipe (`CMakeLists.txt`)

This is where you tell CMake what to do.

```cmake
# 1. Always start with this. It's like a version number for the rulebook.
cmake_minimum_required(VERSION 3.10)

# 2. Name your project. This is important for organization.
project(HelloCMake)

# 3. Tell it what C++ standard you're using. Modern C++ is good for the soul.
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 4. The main event: create an executable named "hello_cmake" from our source file.
add_executable(hello_cmake main.cpp)
```

### Step 4: Build and Run

⚠️ **Pro Tip: Out-of-Source Builds**
Never, ever run `cmake .` in your source directory. Always create a `build` directory. This keeps all the generated junk separate from your precious code.

```bash
# 1. Configure: Create the build files in a `build` directory.
cmake -S . -B build

# 2. Build: Run the actual compiler.
cmake --build build

# 3. Run: The executable is waiting for you in the build folder.
./build/hello_cmake
```

You should see `Hello, CMake!` printed to your terminal. You've done it! You've tamed your first beast. 🎉

## 🗺️ Level 3: Finding External Libraries

Your project isn't an island. You'll need other libraries. `find_package` is CMake's way of sending out a search party.

Let's find the popular {fmt} formatting library.

```cmake
# Ask CMake to find the {fmt} library.
# The CONFIG keyword is the modern, preferred way.
find_package(fmt CONFIG REQUIRED)

# If it's found, a target named `fmt::fmt` is created automatically.
# Now we can just link to it!
target_link_libraries(greeter_app PRIVATE fmt::fmt)
```

Now you can use it in your code:

**`src/main.cpp`**
```cpp
#include "greeter.h"
#include <fmt/core.h>

int main() {
    greet("World");
    fmt::print("This is a formatted message from the {fmt} library!\n");
    return 0;
}
```

## 🏅 Best Practices: The Antigravity Way

-   **Always Out-of-Source:** I'm saying it again. `cmake -S . -B build`. Burn it into your brain.
-   **Modern is Better:** Use `target_*` commands. They are more precise and prevent so many headaches. If you see someone using `include_directories()` without `target_`, tell them a friendly senior engineer sent you.
-   **Use `.gitignore`:** Your `build` directory should never be in git.
-   **Stale Cache? Nuke it:** If CMake is acting weird, `rm -rf build` and start over. It's the fastest way to fix 90% of strange configuration problems.


