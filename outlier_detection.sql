WITH Yearly_Counts AS (
    SELECT 
        "Year", 
        COUNT(*) AS num_observations
    FROM 
        video_game_sales
    GROUP BY 
        "Year"
),
Total_Observations AS (
    SELECT 
        COUNT(*) AS total_observations
    FROM 
        video_game_sales
),
Filtered_Years AS (
    SELECT 
        yc."Year"
    FROM 
        Yearly_Counts yc,
        Total_Observations tobs
    WHERE 
        yc.num_observations >= 0.045 * tobs.total_observations
)
SELECT 
    DISTINCT vg.Year
FROM 
    video_game_sales vg
JOIN 
    Filtered_Years fy
ON 
    vg."Year" = fy."Year";
