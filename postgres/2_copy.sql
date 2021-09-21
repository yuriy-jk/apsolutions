COPY posts(text, created_date, rubrics)
FROM '/api/posts.csv'
DELIMITER ','
CSV HEADER;