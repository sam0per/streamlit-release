import streamlit as st
import traceback

st.set_page_config(page_title="Enhanced Exception Handling", page_icon="🐞")

st.title("🐞 Enhanced Exception Handling")
st.markdown("""
Streamlit v1.44.0 enhances how exceptions are displayed with the `st.exception` component.
Now, exceptions include helpful links to find solutions on Google or ChatGPT.
""")

st.divider()

st.subheader("Demonstration")
st.markdown("""
Below are some examples of how the enhanced exception handling works.
Click the buttons to generate different types of exceptions.
""")

if st.button("Show Division by Zero Error"):
    try:
        result = 1 / 0
    except Exception as e:
        st.exception(e)
        
if st.button("Show Type Error"):
    try:
        result = "2" + 2  # Type error: can't concatenate str and int
    except Exception as e:
        st.exception(e)

if st.button("Show Import Error"):
    try:
        import non_existent_module
    except Exception as e:
        st.exception(e)

st.divider()

st.subheader("Custom Exception Display")
st.markdown("""
You can also catch exceptions in your code and display them with `st.exception`.
This gives you more control over error handling in your app.
""")

code = st.text_area(
    "Try running this code (it has an error):",
    '''
def calculate_percentage(value, total):
    return (value / total) * 100

# This will fail if user enters 0
user_total = 0
result = calculate_percentage(50, user_total)
print(f"The percentage is {result}%")
    '''
)

if st.button("Run Code"):
    try:
        # Execute the user's code
        exec(code)
    except Exception as e:
        st.error("The code generated an error:")
        st.exception(e)
        st.info("Notice the Google and ChatGPT links above - these are new in v1.44.0!")

st.code('''
# How to use st.exception in your code:
try:
    # Your code that might raise an exception
    result = 1 / 0
except Exception as e:
    st.exception(e)  # Display with helpful links
''')