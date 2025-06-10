import streamlit as st
from streamlit_option_menu import option_menu
st.title("🚀Vinsup Infotech")
# with st.sidebar:
#     st.header("🚀Vinsup Infotech")
# st.write("_vinsup_")
# st.write("# vinsup")
# st.write(" ## vinsup")
# st.write("- vinsup ")
# st.text_input("Enter your name")
# st.button("submit")
with st.sidebar:
    data=option_menu(
        menu_title="vinsup",
        options=["Home","About","Contact"],
        icons=["house","people","phone"])
if data=="Home":
    st.header("Registration Form")
    

    col1,col2=st.columns(2)
    with col1:
        Name=st.text_input("Enter your Name")
        Email=st.text_input("Enter your Email")
    with col2:
         Phone= st.text_input("Enter your Number")
         Password=st.text_input("Enter your Password")
    if st.button("Submit"):
        st.write(Name,Email,Phone,Password)
        st.success("Data inserted Successfully ")
        st.balloons()
        # st.snow()
    st.metric(label="python",value=20,delta="20%")
    st.number_input("Integer",max_value=0)
    st.radio(label=":rainbow[Gender]",options=["Male","Female"])
    st.multiselect(label="City",options=["Madurai","Chennai","Trichy"])
    st.slider("Numbers",0,100)
    st.file_uploader("Upload")


elif data=="About":
    st.header("About Page")
elif data=="Contact":
    st.header("Contact Page")
   
             
    