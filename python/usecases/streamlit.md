# 🚀 Usecase: Building Web Apps with `streamlit`

You've written a Python script to analyze a dataset, visualize some results, or make predictions with a model. Now, how do you share it? You could ask people to run your script, but a web app is much more user-friendly. The problem is, building web apps is usually complex.

**Streamlit** changes everything. It's an open-source Python library that makes it incredibly simple to create and share beautiful, custom web apps for machine learning and data science. If you can write a Python script, you can build a Streamlit app.

---

## 🎯 Streamlit: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install Streamlit =====
# pip install streamlit pandas matplotlib

# ===== 2. Basic App Structure =====
import streamlit as st
st.title("Hello Streamlit!")
st.write("This is a simple web app.")

# ===== 3. File Upload and DataFrame =====
import pandas as pd
uploaded = st.file_uploader("Upload CSV", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df)

# ===== 4. Interactive Widgets =====
name = st.text_input("Your name:")
st.write(f"Hello, {name}!")
value = st.slider("Pick a value", 0, 100, 50)
st.write(f"Slider value: {value}")

# ===== 5. Plotting =====
import matplotlib.pyplot as plt
if uploaded:
    col = st.selectbox("Column for histogram", df.columns)
    bins = st.slider("Bins", 5, 50, 20)
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=bins)
    st.pyplot(fig)

# ===== 6. Sidebar Widgets =====
st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose", ["A", "B", "C"])
st.sidebar.write(f"You picked: {option}")

# ===== 7. Fun: Data Exploration App =====
if uploaded:
    st.header("Describe Data")
    st.write(df.describe())

# ===== 8. Pro-Tips =====
# Use @st.cache_data for caching
# Use st.columns for layout
# Use st.button, st.checkbox, st.radio for more interactivity
# Use Streamlit Community Cloud for free deployment
```
