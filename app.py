import streamlit as st
import pandas as pd
import pickle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("AI_FUSION.jpg", caption="Hackathon")
st.title('Loan Prediction Interface')

pin_code = st.selectbox('Pin-code', ['Select', '110001', '110003', '110004','110011','110014'])
age = st.slider('Age', min_value=21, max_value=65, step=1, value=30)
fam_members = st.selectbox('Family Members', ['1', '2', '3', '4+'])
education = st.selectbox('Education Level', ['Under Graduate', 'Post Graduate', 'Graduate'])
t_experience = st.slider('Total Experience (in years)', min_value=0, max_value=40, step=1, value=5)
income = st.number_input('Monthly Income', min_value=0, step=1000)
mortgage = st.number_input('Mortgage', min_value=0, step=1000)
fixed_deposit = st.selectbox('Fixed Deposit', ['Yes', 'No'])
demat = st.selectbox('Demat Account', ['Yes', 'No'])
net_banking = st.selectbox('Net Banking', ['Yes', 'No'])


if st.button('Predict Loan'):
    # Preprocessing
    age=(age-21)/44
    t_experience=(t_experience+3)/46
    income=(income-64000)/1728000
    mortgage=mortgage/5080000

    pin={'110001':0,'110003':1,'110004':2,'110011':3,'110014':4}
    common={'No':0,'Yes':1}
    edu={'Under Graduate':0,'Post Graduate':1,'Graduate':2}
    pin_code=pin[pin_code]
    fixed_deposit=common[fixed_deposit]
    demat=common[demat]
    net_banking=common[net_banking]


    input_data = pd.DataFrame({
        'Pin-code': [pin_code],
        'age': [age],
        'Fam members': [fam_members],
        'Education': [education],
        'T.Experience': [t_experience],
        'Income': [income],
        'Mortgage': [mortgage],
        'Fixed Deposit': [fixed_deposit],
        'Demat': [demat],
        'Net Banking': [net_banking]
    })
    input_data=input_data.astype({'Fam members':"category",'Education':"category",'Fixed Deposit':"category",'Demat':"category",'Net Banking':"category"})
    prediction = model.predict(input_data)
    st.write(f'Loan Prediction: {"Will Accept" if prediction[0] == 1 else "Will Not Accept"}')
