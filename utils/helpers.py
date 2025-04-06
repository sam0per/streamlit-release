import streamlit as st

def display_theme_config():
    """Display the current theme configuration options."""
    theme_config = """
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#F0F2F6"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#262730"
font = "Roboto"
baseFontSize = 16
cornerRadius = 8
"""
    return theme_config

def simulate_exception(exception_type="zero_division"):
    """Generate a sample exception for demonstration."""
    try:
        if exception_type == "zero_division":
            return 1 / 0
        elif exception_type == "type_error":
            return "2" + 2
        elif exception_type == "index_error":
            return [1, 2, 3][10]
        else:
            raise ValueError(f"Unknown exception type: {exception_type}")
    except Exception as e:
        return e