CREATE DATABASE dbname;
CREATE USER dbuser WITH PASSWORD 'dbpass';
ALTER ROLE dbuser SET client_encoding TO 'utf8';
ALTER ROLE dbuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE dbuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dbname TO dbuser;
