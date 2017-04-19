SELECT DATE(datetime), COUNT(DISTINCT user_id)
FROM metrics
WHERE datetime >= '2000-01-01'
AND datetime < '2010-01-01'
GROUP BY 1
ORDER BY 1
