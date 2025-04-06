import streamlit as st

st.set_page_config(page_title="Advanced Theming", page_icon="🎨")

st.title("🎨 Advanced Theming Options")
st.markdown("""
Streamlit v1.44.0 introduces enhanced theming capabilities that allow you to customize 
your app's appearance without writing CSS.
""")

st.code('''
# In .streamlit/config.toml:
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#F0F2F6"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#262730"
font = "Roboto"        # New in v1.44.0!
baseFontSize = 16      # New in v1.44.0!
cornerRadius = 8       # New in v1.44.0!
''', language="toml")

with st.expander("How Theme Configuration Works"):
    st.markdown("""
    ### New Theme Options in v1.44.0
    
    - **font**: Specify the font family for your app
        - Options include: "sans serif", "serif", "monospace", or specific fonts like "Roboto"
    
    - **baseFontSize**: Set the base font size (in px) for text elements
        - Recommended range: 14-18px
    
    - **cornerRadius**: Control the roundness of UI elements (in px)
        - Higher values create more rounded corners
    """)

st.divider()

st.subheader("Interactive Theme Preview")
col1, col2 = st.columns(2)

with col1:
    font = st.selectbox(
        "Font Family",
        ["Roboto", "sans serif", "serif", "monospace", "Source Sans Pro"]
    )
    
    font_size = st.slider("Base Font Size (px)", 12, 24, 16)

with col2:
    corner_radius = st.slider("Corner Radius (px)", 0, 20, 8)
    primary_color = st.color_picker("Primary Color", "#FF4B4B")

st.markdown("### Preview")
st.info(f"This is how elements would look with font '{font}', size {font_size}px, and corner radius {corner_radius}px")
st.button("Example Button")
st.slider("Example Slider", 0, 100, 50)

st.caption("Note: This is just a visual representation. To actually change the theme, edit .streamlit/config.toml")