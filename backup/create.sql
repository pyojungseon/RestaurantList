create table ContextTable
(
id nvarchar(100) not null,
tag nvarchar(10) not null,
lifespan int not null,
text nvarchar(1000),
finish nvarchar(1) not null,
regDate timestamp,
modDate timestamp
);