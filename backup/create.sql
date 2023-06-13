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


create table SugTBL
(
id nvarchar(100) not null,
text nvarchar(1000),
regDate timestamp
);


create table RestTBL
(
seq int NOT NULL AUTO_INCREMENT,
name nvarchar(1000) not null,
tag nvarchar(10),
menu nvarchar(200),
lprice int,
hprice int,
map nvarchar(1000),
moksung nvarchar(1),
payco nvarchar(1),
mn5 nvarchar(1),
mn4 nvarchar(1),
mn2 nvarchar(1),
eval nvarchar(2000),
regDate timestamp,
modDate timestamp,
primary key(seq)
);

ALTER TABLE RestTBL ADD eval varchar(2000) AFTER mn2;
ALTER TABLE RestTBL ADD menu varchar(200) AFTER tag;