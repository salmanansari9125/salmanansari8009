import streamlit as st
st.title("Welcome to Salman Ansari Website")
st.header("I Love Python")
name = st.text_input("Enter Your Name: ")
fname = st.text_input("Enter Your Father Name: ")
adr = st.text_area("Enter Your Address: ")
classdata = st.selectbox("Enrer Your Class: ",(1,2,3,4,5,6,7,8,9,10,11,12))
button = st.button("Done")
if button:
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    Address : {adr}
    Class : {classdata}""")