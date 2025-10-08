
  
    

create or replace transient table USER_ACTIVITY_DB.ANALYTICS.fct_posts
    
    
    
    as (SELECT
    p.post_id,
    p.user_id,
    p.title,
    c.number_of_comments
FROM USER_ACTIVITY_DB.ANALYTICS.stg_posts p
LEFT JOIN USER_ACTIVITY_DB.ANALYTICS.int_comments_per_post c
    ON p.post_id = c.post_id
    )
;


  