# Python Internationalization Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to internationalization.

---

## gettext — Multilingual Internationalization Services

**Description:**  
Provides internationalization (I18N) and localization (L10N) support for your Python programs, including message translation.

**Usage Example:**
```python
import gettext

# Set up message catalog access
gettext.install('myapp', localedir='locales')

print(_('Hello, world!'))  # Translated string if available
```

---

## locale — Internationalization Services

**Description:**  
Provides access to POSIX locale databases and functionality for formatting numbers, dates, and currencies according to locale.

**Usage Example:**
```python
import locale

locale.setlocale(locale.LC_ALL, '')
print(locale.currency(1234.56))  # Currency formatted according to current locale
print(locale.format_string('%d', 1234567, grouping=True))  # '1,234,567' (in en_US)
```

---
