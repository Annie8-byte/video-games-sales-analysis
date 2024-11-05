BUCKET_S3 = "videogame-sales-analysis-vskrjenv45t3534"
DATA_FILE_S3_URI = f"s3://{BUCKET_S3}/vgsales.csv"
QUERY_PATH_BASED_ON_CATEGORY = {
    "outliers":"outlier_detection.sql",
    "sales_by_category":"sales_by_category.sql",
}