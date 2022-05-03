#To create a title for the app:
import streamlit as st
st.title("Hello")

#To Create a header and sub-header:
st.header("Header")
st.subheader("sub-header")

#To create a text:
st.text("Enter the text to be displayes in your web app")
#Note: text command cannot change the font of the text

#For text size
st.markdown(''' #h1tag
                ##tag ''')
#Note:This works similar to the html tags, and hash indicates the size of the text.

#To add emojis to your text:
st.markdown(''':moon:''')
st.markdown(''':moon:<br>:sunglasses:**bold**''',true)
#Note: ** for the text to be in bold and - for the text to be in italics.


