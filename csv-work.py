import pandas as pd
import streamlit as st

"""
with open("data.csv", "r") as file:
    # print(file.read()) -> tanpa pandas
    csv = pd.read_csv(file)
    print(csv)
"""

with open("data.csv", "r") as file:
    csv = pd.read_csv(file)

    st.write("### Data Employe")
    st.dataframe(csv)

    st.bar_chart(csv.set_index("city")["salary"])