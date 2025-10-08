SELECT
    raw_json:postId::INT AS post_id,
    raw_json:id::INT AS comment_id,
    raw_json:name::STRING AS name,
    raw_json:email::STRING AS email,
    raw_json:body::STRING AS body
FROM USER_ACTIVITY_DB.RAW_DATA.comments