# Python Cryptographic Services Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to cryptography.

---

## hashlib — Secure Hashes and Message Digests

**Description:**  
Provides functions for creating secure hash and message digest algorithms, such as SHA and MD5.

**Usage Example:**
```python
import hashlib

data = b"hello"
sha256 = hashlib.sha256(data).hexdigest()
print(sha256)  # SHA-256 hash of 'hello'
```

---

## hmac — Keyed-Hashing for Message Authentication

**Description:**  
Implements keyed-hashing for message authentication using HMAC (Hash-based Message Authentication Code).

**Usage Example:**
```python
import hmac
import hashlib

key = b'secret'
msg = b'hello'
h = hmac.new(key, msg, hashlib.sha256)
print(h.hexdigest())  # HMAC-SHA256 of 'hello' with key 'secret'
```

---

## secrets — Generate Secure Random Numbers for Managing Secrets

**Description:**  
Provides functions for generating cryptographically strong random numbers and tokens, suitable for managing secrets.

**Usage Example:**
```python
import secrets

token = secrets.token_hex(16)
print(token)  # 32-character random hex string

number = secrets.randbelow(100)
print(number)  # Random integer in [0, 100)
```

---
