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
    
    # Add practical formatting examples
    import locale
    from datetime import datetime
    import babel.core
    from babel.numbers import format_currency, format_decimal
    from babel.dates import format_date
    
    # Example date
    current_date = datetime.now()
    
    # UK formatting (for comparison)
    uk_format = "en_GB"
    uk_date = format_date(current_date, format='long', locale=uk_format)
    uk_number = format_decimal(1234567.89, locale=uk_format)
    uk_currency = format_currency(1234.56, 'GBP', locale=uk_format)
    
    # User's locale formatting
    # Convert hyphen to underscore for compatibility
    babel_locale = user_locale.replace('-', '_')
    
    try:
        # Use babel for more robust international formatting (doesn't rely on system locales)
        local_date = format_date(current_date, format='long', locale=babel_locale)
        local_number = format_decimal(1234567.89, locale=babel_locale)
        
        # Determine appropriate currency based on region if available
        if "-" in user_locale:
            language, region = user_locale.split("-", 1)
            if region == "US":
                currency_code = "USD"
            elif region == "GB":
                currency_code = "GBP"
            elif region in ["DE", "FR", "IT", "ES"]:
                currency_code = "EUR"
            elif region == "JP":
                currency_code = "JPY"
            elif region == "CN":
                currency_code = "CNY"
            elif region == "CA":
                currency_code = "CAD"
            elif region == "AU":
                currency_code = "AUD"
            else:
                currency_code = "USD"  # Default
        else:
            currency_code = "USD"  # Default
            
        local_currency = format_currency(1234.56, currency_code, locale=babel_locale)
        
        st.write("### Formatting Comparison")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### UK Format (en_GB)")
            st.write(f"**Date:** {uk_date}")
            st.write(f"**Number:** {uk_number}")
            st.write(f"**Currency:** {uk_currency}")
            
        with col2:
            st.markdown(f"#### Your Locale ({user_locale})")
            st.write(f"**Date:** {local_date}")
            st.write(f"**Number:** {local_number}")
            st.write(f"**Currency:** {local_currency}")
    
    except (ValueError, babel.core.UnknownLocaleError) as e:
        st.warning(f"Could not apply locale formatting for {user_locale}: {str(e)}")
        st.info("Falling back to default formatting")
        
        # Fallback to basic formatting
        st.write("### Formatting Comparison")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### UK Format (en_GB)")
            st.write(f"**Date:** {uk_date}")
            st.write(f"**Number:** {uk_number}")
            st.write(f"**Currency:** {uk_currency}")
            
        with col2:
            st.markdown(f"#### Basic Format (Fallback)")
            st.write(f"**Date:** {current_date.strftime('%Y-%m-%d')}")
            st.write(f"**Number:** {'{:,.2f}'.format(1234567.89)}")
            st.write(f"**Currency:** ${'{:,.2f}'.format(1234.56)}")
        
except AttributeError:
    st.warning("This feature requires Streamlit v1.44.0 or higher. You seem to be running an older version.")
    st.info("In actual v1.44.0, you would see your detected locale here.")
    # Mock implementation for demonstration
    st.success("Mock locale for demo: **en-US**")
    
    # Mock formatting example for demo
    st.write("### Formatting Comparison (Mock Demo)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### UK Format (en_GB)")
        st.write("**Date:** 6 April 2025")
        st.write("**Number:** 1,234,567.89")
        st.write("**Currency:** £1,234.56")
        
    with col2:
        st.markdown("#### US Format (en-US)")
        st.write("**Date:** April 6, 2025")
        st.write("**Number:** 1,234,567.89")
        st.write("**Currency:** $1,234.56")

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