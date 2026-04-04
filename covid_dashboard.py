import streamlit as st
import pandas as pd


data = pd.read_csv("coronavirus_daily_data.csv")

data["date"] = pd.to_datetime(data["date"])


st.title("COVID-19 Global Dashboard")

country = st.selectbox("Select Country", data["country"].unique())


filtered = data[data["country"] == country]

# 1.Total Cases Over Time
st.subheader("Total Cases Over Time")
st.line_chart(filtered.set_index("date")["cumulative_total_cases"])

# 2.Daily New Cases
st.subheader("Daily New Cases")
st.line_chart(filtered.set_index("date")["daily_new_cases"])

# 3. Daily New Deaths
st.subheader("Daily New Deaths")
st.line_chart(filtered.set_index("date")["daily_new_deaths"])

#4. Top 10 Countries by Total Cases
st.subheader("Top 10 Countries by Total Cases")

top_countries = (
    data.groupby("country")["cumulative_total_cases"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_countries)

# 5.Country Comparison
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
