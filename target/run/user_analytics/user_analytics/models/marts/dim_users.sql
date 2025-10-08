
  
    

create or replace transient table USER_ACTIVITY_DB.ANALYTICS.dim_users
    
    
    
    as (SELECT DISTINCT
    user_id
FROM USER_ACTIVITY_DB.ANALYTICS.stg_posts
    )
;


  