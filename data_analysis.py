import pandas as pd 
import streamlit as st
import plotly.express as px

st.title("Goal Keeping")


#create a data frame
df = pd.read_csv("goalkeeping.csv")

#st.write(df)


#code for Data inspection
st.markdown("### Display First Five Items ") 
hope = df.head(5)
st.write(hope)
#displaying the end of a table data 

 
#code for Data inspection
st.markdown("### Display last five Items ")
hall = df.tail()
st.write(hall)

#displaying general information about data
#code for Data inspection
st.markdown("### General Information About Goal Keeping")
hall = df.describe()
st.write(hall)


#displaying number of observation as to rows and columns
#code for Data inspection
st.markdown("### General Information About Goal Keeping")
hall = df.shape
st.table(hall)

#code to pick a column in a table - univariate 
goal = df["saved"].describe()
st.markdown("# UNIVARIATE ANALYSIS")
st.markdown("### Goals Saved by the Keeper")
st.write(goal)

conceded_goal = df["conceded"].describe()
st.markdown("### CONCEDED GOALS BY THE KEEPER")
st.write(conceded_goal)


st.title("Graph Representation")
saved = px.histogram(df["saved"], x = "saved", title = "goals")
st.plotly_chart(saved, use_container_width = True)

#display string type data using bar chart
st.title("Bar Graph Representation")
player_count = df["player_name"].value_counts()
player_count.columns = ["player_name", "counts"]
saved2 = px.bar(df["player_name"], x = "player_name", title = "goals")
st.plotly_chart(saved2, use_container_width = True)

#display arguments using pie chart

st.title("Pie Chart")

st.title('Saved Goals')
counted = df["saved"].value_counts().reset_index()
counted.columns = ["saved", "count"]
saved2 = px.pie(counted, names = "saved", values = "count", title = "Goals")
st.plotly_chart(saved2, use_container_width = True)
