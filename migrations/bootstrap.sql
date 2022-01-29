start transaction;
  create table if not exists stuff (
    id bigserial primary key,
    name text unique not null,
    age int not null
  );
  
  insert into stuff (name, age) values
    ('Potat', 23),
    ('Tomat', 19)
  ;
commit;