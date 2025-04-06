# Streamlit v1.44.0 Features Demo

This application demonstrates the new features introduced in Streamlit v1.44.0.

## Features Showcased

- **Advanced Theming Options**: Custom fonts, sizes, and roundness
<img src="https://github.com/user-attachments/assets/42a64ba1-ed08-4b8e-a700-4a7ac040f5e0" width="300" alt="Theming Options">

- **st.badge Element**: Colored badges for status indicators
<img src="https://github.com/user-attachments/assets/6f18d9cf-ec10-4206-9449-e2d61fa06b12" width="300" alt="Colored Badges">

- **Streamlined Initialization**: The new `streamlit init my_new_app` command generates all the necessary local files for a new app:
   - Creates a basic app.py file
   - Generates a .streamlit folder with config.toml
   - Sets up a requirements.txt file
   - Creates a README.md template

- **Enhanced Exception Handling**: Better error displays with helpful links to Google and ChatGPT
<img src="https://github.com/user-attachments/assets/69e01173-4935-4ffc-84a1-fda2226d3f8d" width="300" alt="Exception Handling">

- **User Locale Access**: Access user's locale via `st.context`
<img src="https://github.com/user-attachments/assets/76326de7-19b5-4725-a14f-60670956c1ad" width="300" alt="Locale Access">

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
