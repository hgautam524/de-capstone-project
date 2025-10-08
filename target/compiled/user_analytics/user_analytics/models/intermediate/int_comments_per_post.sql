SELECT
    post_id,
    COUNT(comment_id) AS number_of_comments
FROM USER_ACTIVITY_DB.ANALYTICS.stg_comments
GROUP BY post_id