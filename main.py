import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

df = pd.DataFrame({
  'Account Name': ["Barclays Bank", "Barclays Saver", "Money Box LISA",
                   "Money Box Cash ISA","Money Box Simple Saver", "IG Stock & Share ISA",
                   "IG Stock & Share"],
  'second column': [10, 20, 30, 40, 4, 6, 7]
})


'sddsd'


st.title("Networth Tracker")

df

st.dataframe()

st.table()


