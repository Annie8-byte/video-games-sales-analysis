SELECT Year, Genre, 
    SUM(NA_Sales) AS Total_NA_Sale,
    SUM(EU_Sales) AS Total_EU_Sales,
    SUM(JP_Sales) AS Total_JP_Sales,
    SUM(Other_Sales) AS Total_Other_Sales,
    SUM(Global_Sales) AS Total_Global_Sales
FROM video_game_sales
WHERE 1=1
GROUP BY Year, Genre
