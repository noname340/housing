import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median Housing Price (Millions):', 0, 500001, 20000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults
income_level = st.sidebar.radio(
    "select income level"
    ('low','medium','high')
)

# filter by population
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximityl.isin(location_filterr)]

if income_level == 'low(≤2.5)':
    filtered_df = df[df['medium_income']<=2.5]
elif income_level == 'medium(> 2.5 & <4.5)':
    filtered_df = df[(df['medium_income']>2.5)&(df['medium_income']<4.5)]
else:
    filtered_df = df[df['medium_income']>4.5]

# show on map
st.map(filtered_df)

# show dataframe
st.subheader('Median House Value')

# show the plot
fig, ax = plt.subplots(figsize=(20, 20))
ax.hist(filtered_df['mediun_house_value'],bins=30)

ax.set_title('Histogram of Median House Value',fontsize=16)
ax.set_xlabel('Median House Value',fontsize=12)
ax.ser_ylabel('Frequency',fontsize=12)

st.pyplot(fig)