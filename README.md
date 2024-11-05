### README.md:

```markdown
# Video Game Sales Analysis & Forecasting

This project analyzes historical video game sales data, performs sales forecasting, and displays results on an interactive Streamlit dashboard. The project leverages AWS for data storage, DuckDB for SQL processing, and FB Prophet for time series forecasting.

## Project Overview

- **Data Source:** [Video Game Sales Dataset](https://www.kaggle.com/datasets/gregorut/videogamesales)
- **Objective:** To analyze and forecast video game sales across different platforms, regions, and genres.

## Technologies Used

- **AWS S3:** Used for storing the video game sales dataset.
- **AWS IAM:** To manage access control and security.
- **AWSwrangler:** For interacting with data stored in S3.
- **DuckDB:** To execute SQL queries and process data.
- **FB Prophet:** For time series forecasting of sales trends. --> WIP
- **Machine Learning:** Used for predicting future sales performance.  --> WIP
- **Streamlit:** To build an interactive dashboard for data visualization.

## Project Workflow

1. **Data Ingestion & Storage:**
   - Upload the dataset to an S3 bucket.
   - Use AWSwrangler to load data from S3 into DuckDB.

2. **Data Processing with DuckDB:**
   - Perform data cleaning and transformation using SQL queries in DuckDB.
   - Aggregate sales data by year, platform, region, and genre.

3. **Forecasting with FB Prophet:**
   - Prepare time series data for forecasting.
   - Train the FB Prophet model to predict future sales trends.

4. **Machine Learning Models:**
   - Apply algorithms like Linear Regression or Decision Trees to predict future sales performance.

5. **Streamlit Dashboard:**
   - Visualize historical and forecasted data.
   - Interactive filters for year, platform, genre, and region.

## Setup Instructions

1. **AWS Setup:**
   - Create an S3 bucket and upload the dataset.
   - Set up an IAM user with read permissions to the bucket.

2. **Python Environment:**
   - Install the required dependencies from `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Project:**
   - Load the data from S3 using AWSwrangler.
   - Process and query the data using DuckDB.
   - Train forecasting models with FB Prophet.
   - Launch the Streamlit dashboard.

   ```bash
   streamlit run app.py
   ```

## Requirements

- Python 3.8+
- `streamlit`
- `awswrangler`
- `duckdb`
- `fbprophet`
- `scikit-learn`
- `boto3`

## Future Enhancements

- Implement more advanced machine learning models.
- Add more interactivity to the Streamlit dashboard.
- Extend forecasting to include more granular time periods (e.g., monthly or weekly).
```

---

This approach ensures you have a well-defined structure for your project, combining multiple technologies in a coherent way. Let me know if you need further adjustments or details!