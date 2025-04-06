import streamlit as st

st.set_page_config(page_title="User Locale Access", page_icon="🌍")

st.title("🌍 User Locale Access")
st.markdown("""
Streamlit v1.44.0 introduces the ability to access the user's locale through the new `st.context` object.
This allows you to create more personalized experiences based on user language and region settings.
""")

st.divider()

st.subheader("Your Locale Information")
try:
    # This is the new feature in v1.44.0
    user_locale = st.context.locale
    
    st.success(f"We detected your locale as: **{user_locale}**")
    
    # Split the locale to get language and region
    if "-" in user_locale:
        language, region = user_locale.split("-", 1)
        st.write(f"**Language:** {language}")
        st.write(f"**Region:** {region}")
    else:
        st.write(f"**Language:** {user_locale}")
        
except AttributeError:
    st.warning("This feature requires Streamlit v1.44.0 or higher. You seem to be running an older version.")
    st.info("In actual v1.44.0, you would see your detected locale here.")
    # Mock implementation for demonstration
    st.success("Mock locale for demo: **en-US**")

st.divider()

st.subheader("Example Use Cases")
st.markdown("""
With access to the user's locale, you can:

- **Translate content** automatically based on user language
- **Format dates and numbers** according to regional preferences
- **Display region-specific information** or customizations
- **Adjust timezone** for time-sensitive information
""")

st.code('''
# Example code using locale information
import streamlit as st
import locale
from datetime import datetime

# Get user locale from st.context
user_locale = st.context.locale

# Set locale for formatting
locale.setlocale(locale.LC_ALL, user_locale)

# Format currency based on user locale
amount = 1234.56
formatted_currency = locale.currency(amount)
st.write(f"Amount in your local format: {formatted_currency}")

# Format date based on user locale
current_date = datetime.now()
formatted_date = current_date.strftime('%x')  # Locale's appropriate date representation
st.write(f"Today's date in your format: {formatted_date}")
''')

st.caption("Note: The actual implementation may need additional libraries like Babel for comprehensive locale support.")