#PURK Calculator

import streamlit as st
 
st.title("Calculate your PURK Score")
st.header("Posterior Urethral valve Risk of chronic Kidney disease (PURK) score is a tool developed at The Hospital for Sick Children (SickKids)")
st.write("It has been externally validated in a cohort of children from Sanjay Gandhi, India.")

# creates a horizontal line
st.write("---")

Option_dict_2 = {"Yes":2, "No":0}
Option_dict_1 = {"Yes":1, "No":0}

def get_value(val,my_dict):
    return new_func(val, my_dict)

def new_func(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value

def get_key(val):
    for key, value in my_dict.items():
        if val == key:
            return value

# input 1
num1 = st.radio ("Baseline Cr >150umol/L (1.7 mg/dL)", tuple(Option_dict_2.keys()))
 
# input 2
num2 = st.radio("Failure to thrive", tuple(Option_dict_2.keys()))
st.caption('Failure to thrive is defined as: failure to regain birthweight within 14 days of birth or presenting with a drop in at least 1 growth curve.')

# input 3
num3 = st.radio("High grade VUR on ultrasound", tuple(Option_dict_1.keys()))
st.caption('High grade defined as grade ≥3')

# input 4
num4 = st.radio("Renal dysplasia on ultrasound", tuple(Option_dict_1.keys()))
 
st.write("Calculate")
 
def calculate():
    ans = get_value(num1,Option_dict_2) + get_value(num2,Option_dict_2) + get_value(num3,Option_dict_1) + get_value(num4,Option_dict_1)
    st.success(f"The PURK score is = {ans}")

 #print the risk of CKD stage ≥3
    if ans == 0:
        st.write("The risk of CKD stage ≥3 is: 0.0% at 1 and 5 years of age")
    elif ans == 1:
        st.write("The risk of CKD stage ≥3 is: 0.0% at 1 year of age and 13.0% at 5 years of age")
    elif ans == 2:
        st.write("The risk of CKD stage ≥3 is: 4.3% at 1 year of age and 22.2% at 5 years of age")
    elif ans == 3:
        st.write("The risk of CKD stage ≥3 is: 42.9% at 1 year of age and 61.5% at 5 years of age")
    elif ans == 4:
        st.write("The risk of CKD stage ≥3 is: 72.0% at 1 year of age and 88.9% at 5 years of age")
    elif ans == 5:
        st.write("The risk of CKD stage ≥3 is: 100.0% at 1 year of age and 100.0% at 5 years of age")
    elif ans == 6:
        st.write("The risk of CKD stage ≥3 is: 100.0% at 1 year of age and 100.0% at 5 years of age")

    st.image('CKD3.png')
    st.caption('Likelihood of CKD stage ≥3 based on PURK Score - a combined cohort of SickKids and Sanjay Gandhi Hospital')

if st.button("Calculate result"):
    calculate()
