import streamlit as st

st.set_page_config(
    page_title="Streamlit v1.44.0 Features Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚀 Streamlit v1.44.0 Features Demo")
st.caption("Released March 25, 2025")

st.markdown("""
This application demonstrates the new features introduced in Streamlit v1.44.0:

1. **Advanced Theming Options** - Customize fonts, colors, and roundness without CSS
2. **st.badge Element** - Add colored badges to your app
3. **Streamlined Initialization** - Create new apps faster with `streamlit init`
4. **Enhanced Exception Handling** - Better exception displays with helpful links
5. **User Locale Access** - Access the user's locale via `st.context`

Use the sidebar to navigate between sections.
""")

st.divider()

st.subheader("New 'streamlit init' Command")
st.markdown("""
Streamlit v1.44.0 introduces a new command: `streamlit init`

This command generates all the necessary local files for a new app:
- Creates a basic app.py file
- Generates a .streamlit folder with config.toml
- Sets up a requirements.txt file
- Creates a README.md template

To use it, simply run:
```bash
streamlit init my_new_app
```

This will create a directory with the starter files to help you get up and running quickly!
""")

# Footer
st.divider()
st.caption("Created to showcase Streamlit v1.44.0 features")