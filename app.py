import streamlit as st
import pandas as pd
import numpy as np
from plotly.io import read_json

st.title('Are you really an activist ?')

def main():
    # Create a text input field
    text_input = st.text_input('Enter your text')

    # Create a submit button
    if st.button('Submit'):
        # Display the entered text using st.write
        st.write('Entered text:', text_input)

if __name__ == '__main__':
    main()


st.title("Engagement Analyses Graph")
option = st.selectbox("Select a personality"
                      ,('BarackObama', 'katyperry', 'cnnbrk', 'YouTube', 'instagram'))
personnality_dict = {
    'Barack Obama':'BarackObama',
    'Katy Pery': 'katyperry'
}

df = pd.read_csv('tweets2.csv')
df_choice = df.query("author==@option")
st.bar_chart(data=df_choice, x='year', y='engagement')


st.plotly_chart(read_json("shape1.json"))

st.plotly_chart(read_json("shape3.json"))
