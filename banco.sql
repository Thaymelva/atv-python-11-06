CREATE DATABASE led_colors;

USE led_colors;

CREATE TABLE colors(
	id int auto_increment primary key,
    color varchar(50),
    timestamp datetime
);

select * from colors