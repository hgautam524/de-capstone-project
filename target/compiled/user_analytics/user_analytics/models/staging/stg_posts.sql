SELECT
    raw_json:userId::INT AS user_id,
    raw_json:id::INT AS post_id,
    raw_json:title::STRING AS title,
    raw_json:body::STRING AS body
FROM USER_ACTIVITY_DB.RAW_DATA.posts