import streamlit as st
import pandas as pd
import numpy as np

st.title("my second cloud app")

st.write("A simple app to demonstrate the use of Streamlit")

df = pd.DataFrame(np.random.randn(10,2),columns=['colo1','col2'])
st.dataframe(df)