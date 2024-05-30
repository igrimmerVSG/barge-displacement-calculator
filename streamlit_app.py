import numpy as np
import pandas as pd
import streamlit as st
import datetime

"""
# Vanc!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
r1c1,r1c2 = st.columns(2)



with r1c1:
    date = st.date_input("Barge load date", value=None)
    st.write("Barge loaded on:", date)

with r1c2:
    barge = st.selectbox("Which barge was loaded?",("MLT4000-2","MLT 4000-4","MLT 4000-5 / MLT 4000-6"))
    st.write("Barge selected: ", barge)

r2c1,r2c2 = st.columns(2)

with r2c1:
    emptyInput = pd.DataFrame(
        {
            'eloc': ['Port Bow', 'Starboard Bow', 'Port Stern', 'Starboard Stern'],
            'eft': [None, None, None, None],
            'ein': [None, None, None, None]
        }
    )

    st.data_editor(
        emptyInput,
        column_config={
            'eloc': 'Measured from: ',
            'eft': st.column_config.NumberColumn(
                'Foot',
                help = 'Please enter the foot measurement for the empty barge at the specified locations!',
                min_value=0,
                max_value=12,
                step=1,
                format='%d', 
            ),
            'ein': st.column_config.NumberColumn(
                'Inch',
                help = 'Please enter the inch measurement for the empty barge at the specified locations!',
                min_value=0,
                max_value=11,
                step=1,
                format='%d', 
            )
        }
    )
with r2c2:
    loadedInput = pd.DataFrame(
        {
            'lloc': ['Port Bow', 'Starboard Bow', 'Port Stern', 'Starboard Stern'],
            'lft': [None, None, None, None],
            'lin': [None, None, None, None]
        }
    )

    st.data_editor(
        loadedInput,
        column_config={
            'lloc': 'Measured from: ',
            'lft': st.column_config.NumberColumn(
                'Foot',
                help = 'Please enter the foot measurement for the loaded barge at the specified locations!',
                min_value=0,
                max_value=12,
                step=1,
                format='%d', 
            ),
            'lin': st.column_config.NumberColumn(
                'Inch',
                help = 'Please enter the inch measurement for the loaded barge at the specified locations!',
                min_value=0,
                max_value=11,
                step=1,
                format='%d', 
            )
        }
    )