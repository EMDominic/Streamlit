import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Kumba Iron Ore Covid-19 Incidence Report")

st.write("Kumba Iron Ore is an iron-ore mining company in South Africa. "
         "It is the fourth largest iron-ore producer in the world and the largest in Africa. "
         "The sites in Kumba are Exploration, Head Office, Kolomela Operations, Saldanha Port Operations, "
         "Kumba SIB Projects, and Sishen. "
         "We investigated Covid incidence in the mines to visualise the trends over time")

# st.write(
#   pd.DataFrame({
#       'A': [1, 2, 3, 4],
#       'B': [5, 6, 7, 8]
#     })
# )

# plotly figure 1
df = px.data.gapminder()
fig1 = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                  size="pop", color="continent", hover_name="country",
                  log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90])

# Display
st.plotly_chart(fig1, use_container_width=True)

st.write("Some inights about the plots here ")

# plotly figure 2
df = px.data.gapminder().query("continent == 'Oceania'")
fig2 = px.line(df, x='year', y='lifeExp', color='country', symbol="country")

# Display
st.plotly_chart(fig2, use_container_width=True)

st.write("Some inights about the plots here ")

st.write("We can also use the web app to display the data as shown below ")

st.write(df)

