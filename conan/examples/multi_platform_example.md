# 🌍 Multi-Platform Conan Example

## Why Use This?
Build a C++ library for Windows, Linux, and macOS using Conan profiles and `conanfile.py` for reproducible, cross-platform builds.

---

## 1. Create and List Profiles
Detect your current platform and see available profiles:
```sh
conan profile detect --force
conan profile list
```
For cross-compilation, create or edit profiles for your target platforms in `~/.conan2/profiles/`.

---

## 2. Build for Different Platforms
### Native build (default profile)
```sh
conan install . --profile:host=default --profile:build=default --output-folder=build --build=missing
conan build . --build-folder=build
```

### Cross-compile (e.g., build Linux binary from Windows)
Make sure you have a cross-compilation profile (e.g., `linux-x86_64`).
```sh
conan install . --profile:host=linux-x86_64 --profile:build=default --output-folder=build-linux --build=missing
conan build . --build-folder=build-linux
```

---

## Troubleshooting & Tips
- If you get errors about missing profiles, create them in `~/.conan2/profiles/` or use `conan profile detect --name=<profile>`.
- Cross-compiling may require additional tools (e.g., MinGW for Windows, aarch64 toolchain for ARM).
- Profiles let you easily switch compilers, architectures, and build types.
- Use `conanfile.py` and `conan build` for reproducible, automated builds across platforms.

---

💡 **Pro Tip:**
- Keep your profiles in version control for consistent builds in CI/CD.
- Use Conan's profiles to quickly test your code on multiple platforms!
