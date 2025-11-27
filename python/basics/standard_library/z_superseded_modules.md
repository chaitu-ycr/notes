# Superseded Python Standard Library Modules

The modules described in this chapter have been superseded by other modules for most use cases and are retained primarily for backwards compatibility.

---

## getopt — C-style Parser for Command Line Options

**Description:**  
Provides a parser for command line options, mimicking the C `getopt()` API.

**Recommended Alternatives:**  
For broader command line option and argument parsing, use `optparse` (deprecated) or `argparse` (preferred).

**Usage Example:**
```python
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output=", "verbose"])
for opt, arg in opts:
	print(opt, arg)
```

---
