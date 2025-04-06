import streamlit as st

st.set_page_config(page_title="st.badge Element", page_icon="🏷️")

st.title("🏷️ New st.badge Element")
st.markdown("""
Streamlit v1.44.0 introduces the `st.badge` element, which allows you to add 
colorful status badges to your app.
""")

st.subheader("Basic Usage")
col1, col2, col3 = st.columns(3)
with col1:
    st.badge("New", color="red")
with col2:
    st.badge("Stable", color="green")
with col3:
    st.badge("Beta", color="blue")

st.code('''
# Basic usage
st.badge("New", color="red")
st.badge("Stable", color="green")
st.badge("Beta", color="blue")
''')

st.divider()

st.subheader("Custom Styling")
col1, col2 = st.columns(2)
with col1:
    st.badge(
        "Premium", 
        color="rainbow",
        icon="⭐"
    )
with col2:
    st.badge(
        "1.44.0", 
        color="orange"
    )

st.code('''
# With custom styling
st.badge(
    "Premium", 
    color="rainbow",
    icon="⭐"
)

st.badge(
    "1.44.0", 
    color="orange"
)
''')

st.divider()

st.subheader("Badges in Markdown")
st.markdown(
    """
You can also use badges directly in markdown using the new directive:

Normal text with a :red-badge[NEW] feature and a :blue-badge[BETA] component.

Code example:
```markdown
Normal text with a :red-badge[NEW] feature and a :blue-badge[BETA] component.
```

This makes it easier to integrate badges with your text content!
"""
)

st.divider()
