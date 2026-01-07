import streamlit as st
import json
import os

st.write("Arbeitsverzeichnis:", os.getcwd())
st.write("Dateien hier:", os.listdir())

with open("watchlists.json", "r") as f:
    content = f.read()
    st.write("Rohinhalt der JSON-Datei:")
    st.write(repr(content))


st.write("TEST")