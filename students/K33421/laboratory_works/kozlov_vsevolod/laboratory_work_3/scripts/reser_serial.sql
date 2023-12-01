CREATE OR REPLACE FUNCTION reset_serial_sequences() RETURNS void AS $$
DECLARE
   name_of_table text;
   name_of_column text;
   sequence_name text;
   max_value bigint;
BEGIN
   FOR name_of_table, name_of_column IN
       SELECT table_name, column_name FROM information_schema.columns
       WHERE column_default LIKE 'nextval%'
   LOOP
       sequence_name := pg_get_serial_sequence(name_of_table, name_of_column);
       if name_of_column is not null then
           EXECUTE format('SELECT max(%I) FROM %I', name_of_column, name_of_table) INTO max_value;
           EXECUTE format('SELECT setval(%L, %s)', sequence_name, max_value + 1);
       end if;
   END LOOP;
END;
$$ LANGUAGE plpgsql;

select *
from lab3_readerroomhistory;

select * from lab3_readerbookhistory;

SELECT table_name, column_name FROM information_schema.columns
                               where table_name like '%lab3%';
