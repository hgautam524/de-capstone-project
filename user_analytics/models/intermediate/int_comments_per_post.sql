SELECT
    post_id,
    COUNT(comment_id) AS number_of_comments
FROM {{ ref('stg_comments') }}
GROUP BY post_id
