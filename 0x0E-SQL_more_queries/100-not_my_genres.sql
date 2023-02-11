-- This script uses the hbtn_0d_tvshows database to
-- list all genres not linked to the show Dexter

-- Use of Join and subquery to get required data
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (
    SELECT tv_genres.name
    FROM tv_genres
    JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows
    ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
