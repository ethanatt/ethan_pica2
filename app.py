import streamlit as st
import requests
from PIL import Image
import io


st.set_page_config(layout="centered", page_icon="🎨", page_title="PICA-2 AI ART")

st.title("🎨 PICA-2")


st.write(
    "Abstract AI Art via Computational Creativity")

left,right = st.columns(2)

left.write("Fill in the data:")
form = left.form("template_form")
color = form.multiselect(
        'Select a Color',
        ['Green', 'Yellow', 'Red', 'Blue'],max_selections = 1)
image1 = form.multiselect(
        'Select your Categories',
        ['Apple', 'Mountain', 'Cloud', 'Butterfly', 'House', 'Door'],max_selections = 2 )
#query = {"color": , "alpha": , "beta": }
right.write("Heres your generated image:")
if form.form_submit_button("Generate Image"):
    alpha = image1[0]
    beta = image1[1]
    color = color[0]
    data = {"alpha": alpha, "beta": beta, "color": color }
    url = f"http://127.0.0.1:8000/super"
    #right.write("Heres your generated image:")
    response = requests.get(url, params=data)

    image = Image.open(io.BytesIO(response.content))
    right.image(image, width = 300) # image will be here with api call



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXMCYn5iGIL9UBihQb5oNUx0JAAZkyD4E5kKcUuJkYPBpu9PVPjPu6s0Ddw863NcV6UZo&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}

         [data-testid="stHeader"] {{
            background-color: #00d4ff00
         }}

         </style>
         """,
         unsafe_allow_html=True
     ) # background (to be changed)

add_bg_from_url()
