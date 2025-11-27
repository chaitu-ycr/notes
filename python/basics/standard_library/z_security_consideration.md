# Security Considerations in Python Standard Library

Certain Python standard library modules have specific security considerations. Review the notes below for each module and general Python security options.

---

## Module-Specific Security Notes

| Module         | Security Consideration |
|----------------|-----------------------|
| base64         | See RFC 4648 for base64 security considerations. |
| hashlib        | All constructors take a `usedforsecurity` keyword-only argument to disable insecure/blocked algorithms. |
| http.server    | Not suitable for production; only basic security checks. |
| logging        | Logging configuration uses `eval()`, which can be unsafe. |
| multiprocessing| `Connection.recv()` uses `pickle`, which is unsafe for untrusted data. |
| pickle         | Restrict globals; unsafe for untrusted sources. |
| random         | Not suitable for security; use `secrets` for cryptographic randomness. |
| shelve         | Based on `pickle`; unsafe for untrusted sources. |
| ssl            | Review SSL/TLS security considerations. |
| subprocess     | Review subprocess security considerations. |
| tempfile       | `mktemp` is deprecated due to race condition vulnerability. |
| xml            | XML parsing can be insecure; review XML security. |
| zipfile        | Malicious .zip files can cause disk volume exhaustion. |

---

## General Python Security Options

- The `-I` command line option runs Python in isolated mode.
- If `-I` cannot be used, use the `-P` option or set the `PYTHONSAFEPATH` environment variable to avoid prepending unsafe paths (current directory, script’s directory, or empty string) to `sys.path`.

---
