import streamlit as st
import pandas as pd
import numpy as np
from plotly.io import read_json
import plotly.express as px

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


qf = pd.read_csv("Final.csv")
tf = qf[['number_of_likes','number_of_shares','sentiment','author']].groupby("author").mean()
tf["auth"]=tf.index
fig = px.scatter(tf, x="number_of_likes", size="number_of_shares", y="sentiment", color="auth", hover_name="number_of_shares", title='Climate change influence for each personnality')
fig.update_layout(xaxis=dict(showgrid=False,
                             zeroline=False),
                  yaxis=dict(showgrid=False,
                             zeroline=False),
                  hovermode="x",
                  showlegend=False
)
fig.update_traces(hovertemplate=None)
st.plotly_chart(fig)
