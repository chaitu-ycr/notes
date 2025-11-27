# 🧪 Usecase: Writing Tests with `pytest`

Writing code is one thing, but how can you be sure it actually works correctly? And more importantly, how can you be sure it *keeps* working correctly after you make changes? The answer is **automated testing**, and `pytest` is the most popular, powerful, and Pythonic framework for doing it.

`pytest` makes writing tests fun. It has a simple, clean syntax and a powerful feature set that scales from small scripts to complex applications.

---

## 🎯 pytest: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install pytest =====
# pip install pytest

# ===== 2. Basic Test Functions =====
def add(a, b):
    return a + b
def is_even(n):
    return n % 2 == 0
def test_add():
    assert add(2, 3) == 5
def test_is_even():
    assert is_even(10)
    assert not is_even(7)

# ===== 3. Fixtures =====
import pytest
@pytest.fixture
def sample_data():
    return [10, 20, 30]
def test_sum(sample_data):
    assert sum(sample_data) == 60
def test_len(sample_data):
    assert len(sample_data) == 3

# ===== 4. Parametrize =====
@pytest.mark.parametrize("n, expected", [(2, True), (7, False), (0, True), (-1, False)])
def test_is_even_cases(n, expected):
    assert is_even(n) == expected

# ===== 5. Exception Testing =====
def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# ===== 6. Fun: Test Coverage =====
# pytest --cov=your_module

# ===== 7. Fun: Temporary Files =====
def test_tmp_file(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"

# ===== 8. Pro-Tips =====
# Use assert for simple tests
# Use fixtures for setup/teardown
# Use parametrize for many cases
# Use pytest.raises for error checks
# Use plugins for coverage, async, web, etc.
```
