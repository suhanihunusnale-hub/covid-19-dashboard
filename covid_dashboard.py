import streamlit as st
import pandas as pd

# Load dataset
data = pd.read_csv("coronavirus_daily_data.csv")

# Convert date column to datetime
data["date"] = pd.to_datetime(data["date"])

# Title
st.title("COVID-19 Global Dashboard")

# Country selector
country = st.selectbox("Select Country", data["country"].unique())

# Filter dataset for selected country
filtered = data[data["country"] == country]

# Graph 1: Total Cases Over Time
st.subheader("Total Cases Over Time")
st.line_chart(filtered.set_index("date")["cumulative_total_cases"])

# Graph 2: Daily New Cases
st.subheader("Daily New Cases")
st.line_chart(filtered.set_index("date")["daily_new_cases"])

# Graph 3: Daily New Deaths
st.subheader("Daily New Deaths")
st.line_chart(filtered.set_index("date")["daily_new_deaths"])

# Graph 4: Top 10 Countries by Total Cases
st.subheader("Top 10 Countries by Total Cases")

top_countries = (
    data.groupby("country")["cumulative_total_cases"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_countries)

# Graph 5: Country Comparison
st.subheader("Compare Countries")

countries = st.multiselect(
    "Select Countries to Compare",
    data["country"].unique(),
    default=["India", "USA"]
)

compare_data = data[data["country"].isin(countries)]

pivot_data = compare_data.pivot(
    index="date",
    columns="country",
    values="cumulative_total_cases"
)

st.line_chart(pivot_data)
