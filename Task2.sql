CREATE PROCEDURE `proc1`( Idate DATE )
BEGIN
    drop table if EXISTS temp_table_proc1;
    CREATE TABLE temp_table_proc1
    as (select s.`name`, s.`cost` - COALESCE(d.discount, 0) as new_price
        from services s
        left join discounts d on s.service_id = d.service_id and d.timefrom <= Idate and d.timeto >= Idate
        where s.timefrom <= Idate and s.timeto >= Idate);
END