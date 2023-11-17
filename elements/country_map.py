import streamlit as st
from PIL import Image


class CountyMap:
    def print_map(self):
        image = Image.open('assets/map.png')
        st.image(image, caption='Top regions over time')
