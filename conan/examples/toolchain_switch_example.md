# 🛠️ Switching Compilers & Toolchains with Conan Profiles

## Why Care?
Want to build your project with GCC, Clang, or MSVC—without changing your code? Conan profiles let you switch compilers and settings in seconds. Great for cross-platform and CI!

---

## 1. Create a Profile for Each Compiler
Run these commands to auto-detect your current compiler and create a profile for each toolchain:
```sh
conan profile detect --name=gcc
conan profile detect --name=clang
conan profile detect --name=msvc
```
Or manually edit profiles in `~/.conan2/profiles/` for custom settings.

---

## 2. Build with a Specific Profile
Use the profile to install dependencies and build for each compiler:
```sh
conan install . --profile=gcc --output-folder=build-gcc --build=missing
conan build . --build-folder=build-gcc

conan install . --profile=clang --output-folder=build-clang --build=missing
conan build . --build-folder=build-clang
```

---

## 3. Troubleshooting & Tips
- If `conan profile detect` fails, check your compiler is in PATH and try again.
- You can customize profiles for different architectures, build types, or flags.
- For CI, keep profiles in your repo and use them for reproducible builds.

---

💡 **Pro Tip:**
Profiles make switching compilers a breeze for cross-platform development and automated CI pipelines!