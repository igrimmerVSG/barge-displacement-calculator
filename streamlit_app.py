import numpy as np
import pandas as pd
import streamlit as st
import datetime

st.logo('Logo.png',icon_image='Logo.png')

st.image('Logo.png')
"""
## Barge Displacement Calculator

"""
r1c1,r1c2 = st.columns(2)



with r1c1:
    date = st.date_input("Barge load date", value=None)
    st.write("Barge loaded on:", date)

with r1c2:
    barge = st.selectbox("Which barge was loaded?",("MLT 4000-2","MLT 4000-4","MLT 4000-5 / MLT 4000-6"))
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

    emptyInputEdit = st.data_editor(
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
    emptySumFt=emptyInputEdit['eft'].sum()
    emptySumIn=emptyInputEdit['ein'].sum()
    emptyAvgM=(emptySumFt+emptySumIn/12)*0.3048/4
    st.write('Average empty freeboard (meters):',emptyAvgM)
with r2c2:
    loadedInput = pd.DataFrame(
        {
            'lloc': ['Port Bow', 'Starboard Bow', 'Port Stern', 'Starboard Stern'],
            'lft': [None, None, None, None],
            'lin': [None, None, None, None]
        }
    )

    loadedInputEdit = st.data_editor(
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
    loadedSumFt=loadedInputEdit['lft'].sum()
    loadedSumIn=loadedInputEdit['lin'].sum()
    loadedAvgM=(loadedSumFt+loadedSumIn/12)*0.3048/4
    st.write('Average loaded freeboard (meters):',loadedAvgM)

def bargeInterpolate(barge):
    match barge:
        case 'MLT 4000-2':
            displacementChart=pd.read_csv('MLT 4000-2.csv')
            emptyDisplacement=displacementChart.iloc[(displacementChart['Freeboard Mean (m)']-emptyAvgM).abs().argsort()[:2]]
            loadedDisplacement=displacementChart.iloc[(displacementChart['Freeboard Mean (m)']-loadedAvgM).abs().argsort()[:2]]
            with r2c1: st.write(emptyDisplacement)
            with r2c2: st.write(loadedDisplacement)
        case 'MLT 4000-4':
            displacementChart=pd.read_csv('MLT 4000-4.csv')
            emptyDisplacement=displacementChart.iloc[(displacementChart['Freeboard Mean (m)']-emptyAvgM).abs().argsort()[:2]]
            loadedDisplacement=displacementChart.iloc[(displacementChart['Freeboard Mean (m)']-loadedAvgM).abs().argsort()[:2]]
            with r2c1: st.write(emptyDisplacement)
            with r2c2: st.write(loadedDisplacement)
        case 'MLT 4000-5 / MLT 4000-6':
            displacementChart=pd.read_csv('MLT 4000-5 & MLT 4000-6.csv')
            if emptyAvgM>displacementChart['Freeboard Mean (m)'].max():
                emptyDisplacement=793
            else:
                emptyDisplacement=displacementChart.iloc[(displacementChart['Freeboard Mean (m)']-emptyAvgM).abs().argsort()[:2]]
            loadedDisplacement=displacementChart.iloc[(displacementChart['Freeboard Mean (m)']-loadedAvgM).abs().argsort()[:2]]
            with r2c1: st.write(emptyDisplacement)
            with r2c2: st.write(loadedDisplacement)

bargeInterpolate(barge)