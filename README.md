# Streamlit v1.44.0 Features Demo

This application demonstrates the new features introduced in Streamlit v1.44.0.

## Features Showcased

- **Advanced Theming Options**: Custom fonts, sizes, and roundness
- **st.badge Element**: Colored badges for status indicators
- **Streamlined Initialization**: The new `streamlit init` command
- **Enhanced Exception Handling**: Better error displays with helpful links
- **User Locale Access**: Access user's locale via `st.context`

## Running the App

1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   streamlit run app.py
   ```

## Structure

- `app.py`: Main entry point
- `pages/`: Individual pages for each feature
- `.streamlit/config.toml`: Theme configuration
- `utils/helpers.py`: Utility functions

## Requirements

- Streamlit v1.44.0 or higher