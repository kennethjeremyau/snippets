UNLOAD ('SELECT * FROM table')
TO 's3://bucket/prefix'
CREDENTIALS 'aws_access_key_id=KEY;aws_secret_access_key=SECRET';

COPY table
FROM 's3://bucket/prefix'
CREDENTIALS 'aws_access_key_id=KEY;aws_secret_access_key=SECRET';
