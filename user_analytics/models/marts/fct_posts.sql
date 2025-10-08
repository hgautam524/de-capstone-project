SELECT
    p.post_id,
    p.user_id,
    p.title,
    c.number_of_comments
FROM {{ ref('stg_posts') }} p
LEFT JOIN {{ ref('int_comments_per_post') }} c
    ON p.post_id = c.post_id

