import streamlit as st 
import numpy as np
import pandas as pd


# Adding title of App
st.title("It's my first app")

# Adding simple text
st.write("enter any text")

# user input
input = st.slider('pick a number', 0, 100, 10)

# print the text of number
st.write(f'You selected: {input}')

# adding a button
if st.button('Greeting'):
    st.write('hello, how are you?')

else:
    st.write("how can i help you")
    
# add radio button
genre = st.radio(
    "what's your favorite movie genre",
    ('comedy','drama', 'Documentary', 'horror')
) 
# print text of genre
st.write(f'You selected: {genre}')   

# add a drop down list
# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Whatsapp', 'other')
# )

# add a drop down list on the left sidebar
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Whatsapp', 'other')
)

# add your contact
st.sidebar.text_input('Enter your contact number')

# add a file uploader
uploaded_file = st.sidebar.file_uploader("Choose a csv file", type="csv")    

# create a linr plot
data = pd.DataFrame({
    'col1': list(range(1,11)),
    'col2': np.arange(input, input+10)
})
st.line_chart(data)
