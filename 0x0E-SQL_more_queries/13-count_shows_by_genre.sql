-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Dont display a genre that doesnt have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT g.name AS genre, COUNT(g.name) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
      ON sg.genre_id = g.id
INNER JOIN tv_shows AS s
      ON sg.show_id = s.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
