# 🌐 Usecase: Opening Web Pages with `webbrowser`

Sometimes, all you need your script to do is open a web page for the user—maybe to show them a documentation site, a report you've just generated, or the login page for a service. You don't need to scrape data or interact with the page, you just need to launch it.

For this simple task, you don't need a heavy automation library like Selenium. Python's built-in `webbrowser` module is the perfect tool for the job.

---

## 🎯 webbrowser: Practical, Tricky, and Fun Usages

```python
# ===== 1. Open a URL =====
import webbrowser
webbrowser.open("https://docs.python.org/3/")

# ===== 2. Open in New Tab/Window =====
webbrowser.open_new_tab("https://www.google.com")
webbrowser.open_new("https://www.bing.com")

# ===== 3. Open Local HTML File =====
import os
html = "<h1>Hello!</h1>"
path = os.path.abspath("hello.html")
with open(path, "w") as f:
    f.write(html)
webbrowser.open(f"file://{path}")

# ===== 4. Specify Browser =====
try:
    chrome = webbrowser.get('chrome')
    chrome.open("https://www.chromium.org")
except webbrowser.Error:
    webbrowser.open("https://www.chromium.org")

# ===== 5. Fun: Open Multiple Pages =====
urls = ["https://python.org", "https://pypi.org", "https://github.com"]
for url in urls:
    webbrowser.open_new_tab(url)

# ===== 6. Pro-Tips =====
# Use file:// for local files
# Use open_new_tab for multiple tabs
# Use try/except for browser selection
# No need for extra dependencies
```
