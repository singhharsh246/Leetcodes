WITH duplicate AS (
SELECT Email,ROW_NUMBER() over ( partition by email order by email) AS rank FROM Person
    ) 
    SELECT
        DISTINCT Email
    FROM duplicate
    WHERE rank > 1
