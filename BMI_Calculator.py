import streamlit as st 
st.title("BMI Calculator 📟")

# take weight input(in kgs)
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
status = st.radio("select your height format: ",('cms','meters', 'feet'))

# compair status value 
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")

elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

else:
    # take height input in feet
    height = st.number_input('Feet')

    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
        
# calculate BMI
if(st.button("Calculate BMI")):
    
    # print BMI index
    st.text("Your BMI index is {}.".format(bmi))
    
    if(bmi <16):
        st.error("You are exteremely Underweight")
    elif(bmi>=16 and bmi < 18.5):
        st.warning("you are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi>=30):
        st.error("Extremely Overweight")
                        
            
            
                               
    