from query_handler import QueryHandler

# Streamlit Dashboard
# I can select the year
# For every year I can see the Total NA Sales by Category
# Pick the right Graph / visualization to provide me insights
# I must be able to clearly recognize which Genre was the best (or which are the top)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")


# Filter distinct years where the amount of the video games published is more than 0.045 of all the amount of the dataset
outliers = QueryHandler(query_category="outliers").df_result
# Show Total N/A,EU,JP,Other and Global sales by YEAR and Genre
sales_by_category = QueryHandler(query_category="sales_by_category").df_result
#Filter all the information where the year of sales_by_category equals to the year of outliers 
filtered_sales_by_category = sales_by_category[sales_by_category.Year.isin(outliers.Year)]

print(filtered_sales_by_category)


# Prepare the data: group by year and genre, and sum the sales for all regions
sales_by_category = filtered_sales_by_category.groupby(['Year', 'Genre'], as_index=False).agg({
    'Total_NA_Sale': 'sum',
    'Total_EU_Sales': 'sum',
    'Total_JP_Sales': 'sum',
    'Total_Other_Sales': 'sum',
    'Total_Global_Sales': 'sum'
})

# Streamlit app starts here
st.title("Video Game Sales Dashboard")

# Year selection
year = st.selectbox("Select Year", options=sorted(filtered_sales_by_category['Year'].astype(int).unique()))

# Filter the data for the selected year
filtered_sales = filtered_sales_by_category[filtered_sales_by_category['Year'] == year].sort_values(by=['Genre'], ascending=False)
col1, col2 = st.columns([2, 1])

with col1: 
    # Plotting the total sales by genre for the selected year
    st.subheader(f"Sales by Genre for {int(year)}")

    # Creating the stacked bar chart
    genres = filtered_sales['Genre']
    na_sales = filtered_sales['Total_NA_Sale']
    eu_sales = filtered_sales['Total_EU_Sales']
    jp_sales = filtered_sales['Total_JP_Sales']
    other_sales = filtered_sales['Total_Other_Sales']

    # Setting up the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Stacked bar chart for different regions
    ax.bar(genres, na_sales, label='Total_NA_Sale', color='skyblue')
    ax.bar(genres, eu_sales, bottom=na_sales, label='Total_EU_Sales', color='orange')
    ax.bar(genres, jp_sales, bottom=na_sales+eu_sales, label='Total_JP_Sales', color='green')
    ax.bar(genres, other_sales, bottom=na_sales+eu_sales+jp_sales, label='Total_Other_Sales', color='red')

    # Adding titles and labels
    ax.set_ylabel("Sales (in millions)")
    ax.set_xlabel("Genre")
    ax.tick_params(axis='x', labelrotation=90)
    ax.set_title(f"Total Sales by Genre in {int(year)}")
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)

with col2:
    # Display the Global Sales in a separate chart or as a table
    st.subheader(f"Total_Global_Sales by Genre in {int(year)}")
    st.dataframe(filtered_sales[['Genre', 'Total_Global_Sales']].sort_values(by=['Total_Global_Sales'], ascending=False), hide_index=True)

# Annotating the top genre
top_genre = filtered_sales.loc[filtered_sales['Total_Global_Sales'].idxmax()]

# Display the best genre
st.subheader(f"Top Genre for {int(year)}: {top_genre['Genre']}")
st.write(f"The genre with the highest Total_Global_Sales in {int(year)} is **{top_genre['Genre']}** with **{top_genre['Total_Global_Sales']:.2f} million** sales.")

# Group the data by Year and Genre, and sum the sales for Global
global_sales_by_year_genre = filtered_sales_by_category.groupby(['Year', 'Genre'], as_index=False).agg({
    'Total_Global_Sales': 'sum'
})

# Streamlit app starts here
st.title("Change in Global Sales by Genre Over the Years")

# Genre selection (Multi-select to allow comparison of multiple genres)
selected_genres = st.multiselect("Select Genres to Compare", options=global_sales_by_year_genre['Genre'].unique(), default=global_sales_by_year_genre['Genre'].unique()[:1],key="Global_genre_multiselect")

# Filter the data based on the selected genres
filtered_sales = global_sales_by_year_genre[global_sales_by_year_genre['Genre'].isin(selected_genres)]

# Plotting the change in NA sales by genre over the years
st.subheader(f"Global Sales Over the Years for Selected Genres")

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot a line for each selected genre
for genre in selected_genres:
    genre_data = filtered_sales[filtered_sales['Genre'] == genre]
    ax.plot(genre_data['Year'], genre_data['Total_Global_Sales'], label=genre, marker='o')

# Adding titles and labels
ax.set_ylabel("Global Sales (in millions)")
ax.set_xlabel("Year")
ax.set_title("Change in Global Sales by Genre Over the Years")
ax.legend(title="Genre")
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# Group the data by Year and Genre, and sum the sales for each region (NA, EU, JP, Other)
sales_by_year_genre = filtered_sales_by_category.groupby(['Year', 'Genre'], as_index=False).agg({
    'Total_NA_Sale': 'sum',
    'Total_EU_Sales': 'sum',
    'Total_JP_Sales': 'sum',
    'Total_Other_Sales': 'sum'
})
# Streamlit app starts here
st.title("Sales Change in NA, EU, JP, and Other Regions Over the Years")

# Genre selection (Multi-select to allow comparison of multiple genres)
selected_genres = st.multiselect("Select Genres to Compare", options=sales_by_year_genre['Genre'].unique(), default=sales_by_year_genre['Genre'].unique()[:1], key="genre_multiselect")

# Filter the data based on the selected genres
filtered_sales = sales_by_year_genre[sales_by_year_genre['Genre'].isin(selected_genres)]

# Plotting the change in sales by genre and region over the years
st.subheader(f"Sales Change Over the Years for Selected Genres")

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot a line for each region (NA, EU, JP, Other) for each selected genre
for genre in selected_genres:
    genre_data = filtered_sales[filtered_sales['Genre'] == genre]
    
    # Plot NA Sales
    ax.plot(genre_data['Year'], genre_data['Total_NA_Sale'], label=f'{genre} - NA', marker='o', linestyle='-', color='skyblue')
    
    # Plot EU Sales
    ax.plot(genre_data['Year'], genre_data['Total_EU_Sales'], label=f'{genre} - EU', marker='o', linestyle='--', color='orange')
    
    # Plot JP Sales
    ax.plot(genre_data['Year'], genre_data['Total_JP_Sales'], label=f'{genre} - JP', marker='o', linestyle='-.', color='green')
    
    # Plot Other Sales
    ax.plot(genre_data['Year'], genre_data['Total_Other_Sales'], label=f'{genre} - Other', marker='o', linestyle=':', color='red')

# Adding titles and labels
ax.set_ylabel("Sales (in millions)")
ax.set_xlabel("Year")
ax.set_title("Sales Change Over the Years by Genre and Region")
ax.legend(title="Genre - Region", loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# Group the data by Year and Genre, and sum the sales for each region (NA, EU, JP, Other)
sales_by_year_genre = filtered_sales_by_category.groupby(['Year', 'Genre'], as_index=False).agg({
    'Total_NA_Sale': 'sum',
    'Total_EU_Sales': 'sum',
    'Total_JP_Sales': 'sum',
    'Total_Other_Sales': 'sum'
})
# Streamlit app starts here
st.title("Percentage Change in Sales by Genre Over the Years")

# Region selection
region = st.selectbox("Select Region for Analysis", options=['Total_NA_Sale', 'Total_EU_Sales', 'Total_JP_Sales', 'Total_Other_Sales'], key="region_select")

# Genre selection (Multi-select to allow comparison of multiple genres)
selected_genres = st.multiselect("Select Genres to Compare", 
                                 options=sales_by_year_genre['Genre'].unique(),
                                 default=sales_by_year_genre['Genre'].unique()[:1],
                                 key="genre_multiselect_region")

# Filter the data based on the selected genres
filtered_sales = sales_by_year_genre[sales_by_year_genre['Genre'].isin(selected_genres)]

# Initialize an empty list to store the results
percentage_change_list = []

# Calculate the percentage change for the selected region and genres
for genre in selected_genres:
    genre_data = filtered_sales[filtered_sales['Genre'] == genre].copy()
    
    # Calculate percentage change for the selected region (e.g., NA_Sales, EU_Sales, etc.)
    genre_data[f'{region}_pct_change'] = genre_data[region].pct_change() * 100  # Multiply by 100 for percentage format
    
    # Append the result to the list
    percentage_change_list.append(genre_data[['Year', 'Genre', f'{region}_pct_change']])

# Concatenate the list of DataFrames into a single DataFrame
percentage_change_data = pd.concat(percentage_change_list, ignore_index=True)

# Plotting the percentage change in sales for the selected region
st.subheader(f"Percentage Change in {region.replace('_', ' ')} Sales Over the Years for Selected Genres")

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot a line for each selected genre
for genre in selected_genres:
    genre_data = percentage_change_data[percentage_change_data['Genre'] == genre]
    ax.plot(genre_data['Year'], genre_data[f'{region}_pct_change'], label=f'{genre}', marker='o')

# Adding titles and labels
ax.set_ylabel(f"Percentage Change in {region.replace('_', ' ')} Sales (%)")
ax.set_xlabel("Year")
ax.set_title(f"Year-over-Year Percentage Change in {region.replace('_', ' ')} Sales by Genre")
ax.legend(title="Genre")
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)