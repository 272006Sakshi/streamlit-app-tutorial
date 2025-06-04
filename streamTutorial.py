import streamlit as st 
 # add title 
st.title("Welcome to Streamlit Tutorial")
# add subheader
st.subheader("This is a simple streamlit app")
# add text
st.text("heyy learners, this is a simple streamlit app to demonstrate the basic features of streamlit")
# addheader
st.header(" Streamlit features")
# markdown
st.markdown("**Streamlit** is a powerful framework for building interactive web application in python")
# add code
# sucess, Info, Warning, Error, Expection:
st.success("Sucess")

st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# write a text
st.text("This is a simple text")

# display image
from PIL import Image

# Correct way to load and display the image
img = Image.open(r"c:\users\hp\OneDrive\Pictures\Saved Pictures\IMG-20240331-WA0074.jpg")
st.image(img, width=200)



if st.checkbox("Show/Hide"):
    st.text("Showing the widget")
else:
    st.text("Hide the widget")
    # add a botton
    if st.button("Click here"):
        st.write("Button was clicked!")
        
# selection box
hobbies = st.multiselect("Enter your hobby:", ["Reading", "Writing", "Coding", "Yoga"])  
st.write("Your hobbies is:", hobbies)     

# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!") 
    
# Text Input

name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)  
    
# slider

level = st.slider("Select the level", 1, 5)

st.text('Selected: {}'.format(level))          

   
        