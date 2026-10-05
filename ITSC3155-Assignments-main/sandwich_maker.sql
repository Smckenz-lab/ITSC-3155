Create Database sandwhich_maker;
Use sandwich_maker;

Create Table resources (
	item varchar(50) Primary Key,
    amount decimal(5,2) Not Null
);

Create Table sandwiches (
	sandwich_size varchar(50) Primary Key ,
    price decimal(5,2)
);

Create Table recipes (
	sandwich_size varchar(50) Not Null,
    item varchar(50) Not Null,
    amount int Not Null,
    Primary Key (sandwich_size, item),
	Foreign Key (sandwich_size) references sandwiches(sandwich_size),
    Foreign Key (item) references resources(item)
);
Insert INTO sandwiches (sandwich_size, price) VALUES
('small', 1.75),
('medium', 3.25),
('large', 5.5);

SELECT * FROM sandwiches;

Insert INTO resources (item, amount) VALUES
('bread', 12),
('ham', 18),
('cheese', 24);

SELECT * FROM resources;

Insert INTO recipes (sandwich_size, item, amount) VALUES
('small', 'bread', 2),
('small', 'ham', 4),
('small', 'cheese', 4),
('medium', 'bread', 4),
('medium','ham', 6),
('medium', 'cheese', 8),
('large', 'bread', 6),
('large','ham', 8),
('large', 'cheese', 12);

SELECT * FROM recipes;