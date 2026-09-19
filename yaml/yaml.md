---
title: "📝 YAML: The Human-Friendly Config Language"
aliases:
  - "📝 YAML: The Human-Friendly Config Language"
---
# 📝 YAML: The Human-Friendly Config Language

Welcome to YAML (a recursive acronym for "YAML Ain't Markup Language")! If you've ever worked with configuration files, CI/CD pipelines, or Docker, you've probably met YAML. It's a data serialization language designed to be incredibly easy for humans to read and write.

This guide will walk you through the core syntax and features of YAML, from simple key-value pairs to more advanced structures, all with practical examples.

## 🔗 Related topics

- [GitHub Actions](../github_actions/github_actions.md) — YAML is the language of workflow automation
- [Jenkins](../jenkins/jenkins.md) — declarative pipelines are also YAML-capable in many use cases
- [Git](../git/git.md) — configuration and automation often live next to repo workflows
- [Python](../python/python.md) — config parsing and automation scripts often consume YAML
- [Integration](../integration/integration.md) — the tooling layer where YAML config is most common

> **Note:**  
> - 🧑‍💻 YAML uses spaces (not tabs) for indentation.  
> - 📏 Indentation defines structure and hierarchy.

## 🚀 Tutorial: Building a `config.yml` File

The best way to learn YAML is to build something real. Let's create a typical configuration file (`config.yml`) for a hypothetical web application.

### Step 1: Basic Key-Value Pairs

Every application needs some basic settings. Let's define the application's name and the port it should run on. This is a simple `key: value` structure.

```yml
# The name of our application
app_name: "My Awesome Web App"

# The port the server will listen on
port: 8080
```

### Step 2: Adding Nested Data (Mappings)

Configurations often have grouped settings, like for a database connection. We can create a nested "object" or "mapping" by indenting key-value pairs under a parent key.

```yml
app_name: "My Awesome Web App"
port: 8080

# Database connection settings
database:
  host: "localhost"
  port: 5432
  user: "db_user"
  password: "secure_password" # In a real app, use secrets management!
```

### Step 3: Using Booleans and Nulls

Let's add a feature flag to enable or disable debugging, and a setting for a feature that isn't configured yet.

```yml
app_name: "My Awesome Web App"
port: 8080

database:
  host: "localhost"
  port: 5432
  user: "db_user"
  password: "secure_password"

# Enable debug mode for development
debug_mode: true

# API key for a service we haven't set up yet
external_api_key: null
```

### Step 4: Adding Lists of Items (Sequences)

Finally, let's define a list of admin users who have special privileges in the application. A list in YAML is a sequence of items, each starting with a hyphen (`-`).

```yml
app_name: "My Awesome Web App"
port: 8080

database:
  host: "localhost"
  port: 5432
  user: "db_user"
  password: "secure_password"

debug_mode: true
external_api_key: null

# A list of admin users
admin_users:
  - "alice"
  - "bob"
  - "charlie"
```

### Final `config.yml`

Congratulations! You've created a complete, easy-to-read configuration file that uses YAML's most common features: key-value pairs, nested objects, booleans, nulls, and lists.

This file is now ready to be loaded by your application to configure its settings.

## 2. 🔤 Syntax Basics

The two most important rules in YAML are about how you structure the file: **indentation** and **comments**. Getting these right is the key to a valid YAML file.

### Indentation & Whitespace

- **Spaces Only:** No tabs allowed.
- **Consistent Indent:** Indentation defines structure.

```yml
key1: value1
key2:
  nestedKey1: nestedValue1
  nestedKey2: nestedValue2
```

**❌ Incorrect (tabs cause errors):**
```yml
key1:
<TAB>nestedKey: value
```

### Comments

- Single-line: `# This is a comment`
- Inline: `name: automotive-test-kit  # Inline comment`

```yml
# This is a comment
name: automotive-test-kit  # Inline comment
```

### Numbers & Type Tags

| Type         | Example                        | Description                        |
|--------------|-------------------------------|------------------------------------|
| Integer      | `age: 30`                     | Whole number 🔢                    |
| Negative     | `temperature: -5`             | Negative integer ❄️                |
| Float        | `height: 5.9`                 | Decimal number 💧                  |
| Scientific   | `speed: 3.0e8`                | Exponential notation 🚀            |
| Hexadecimal  | `color: 0xFF5733`             | Hex number 🎨                      |
| Octal        | `perm: 0755`                  | File permissions 🗂️                |
| Binary       | `bin: 0b101010`               | Binary number 💾                   |
| Explicit Tag | `!!int "42"`, `!!float "3.14"`| Explicit type tags 🏷️              |

### Null

| Representation         | Example                        |
|-----------------------|--------------------------------|
| Explicit `null`       | `preferred_language: null`     |
| Tilde (`~`)           | `shipping_address: ~`          |
| Empty Value           | `phone_number:`                |
| Empty Quotes          | `additional_info: ''`          |

## 5. 🛠️ Advanced Features

### Anchors & Aliases

```yml
defaults: &defaults
  country: 🇮🇳 INDIA
  currency: 💸 RUPEE

location1:
  <<: *defaults
  city: chennai
```

### Complex Keys

```yml
? [first, second]
: "Tuple as a key"
```

### Multi-Document Files

```yml
document2:
  key2: value2
...
```

## 7. 🐍 YAML in Python

### Install PyYAML

```sh
pip install pyyaml
```

### Read YAML

```python
import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

data = read_yaml('example.yaml')
print(data)
```

### Write YAML

```python
import yaml

data = {
    'name': 'automotive-test-kit',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'chennai',
        'zip': 12345
    },
    'hobbies': ['Reading', 'Hiking', 'Coding']
}

def write_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

write_yaml('output.yaml', data)
```

**Sample Output (`output.yaml`):**
```yml
name: automotive-test-kit
age: 30
address:
  street: 123 Main St
  city: chennai
  zip: 12345
hobbies:
- Reading
- Hiking
- Coding
```

---

## 8. 🗂️ Quick Reference

- **Indentation:** Use spaces, not tabs.
- **Comments:** Start with `#`.
- **Strings:** Plain, single-quoted, double-quoted, multiline (`|` or `>`).
- **Numbers:** Integer, float, hex, octal, binary.
- **Booleans:** `true`/`false`, `yes`/`no`, `on`/`off`.
- **Null:** `null`, `~`, empty value, `''`.
- **Lists:** Use `-` for each item.
- **Dictionaries:** `key: value` pairs.
- **Anchors/Aliases:** `&anchor`, `*alias`.
- **Multi-document:** Separate with `---`.


