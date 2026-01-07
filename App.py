import streamlit as st
import json
import os

APP_PASSWORD = st.secrets["APP_PASSWORD"]

# Eingabe
password = st.text_input("Passwort eingeben:", type="password")

# Prüfen
if password != APP_PASSWORD:
    st.warning("❌ Falsches Passwort")
    st.stop()  # Alles darunter wird blockiert

# Alles, was privat sein soll, kommt hier
st.write("Arbeitsverzeichnis:", os.getcwd())
st.write("Dateien hier:", os.listdir())

with open("watchlists.json", "r") as f:
    content = f.read()
    st.write("Rohinhalt der JSON-Datei:")
    st.write(repr(content))

st.write("TEST 2")