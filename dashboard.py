import streamlit as st 
import pandas as pd
 
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))