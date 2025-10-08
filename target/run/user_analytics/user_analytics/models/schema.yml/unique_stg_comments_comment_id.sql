
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    comment_id as unique_field,
    count(*) as n_records

from USER_ACTIVITY_DB.ANALYTICS.stg_comments
where comment_id is not null
group by comment_id
having count(*) > 1



  
  
      
    ) dbt_internal_test