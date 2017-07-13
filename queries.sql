/* this is script record some queries i used to discovery the database */

-- check how many articles
select count(id) as num from articles; -- 8

-- check how many authors
select count(id) as num from authors; -- 4

-- check how many logs
select count(id) as num from log; -- 1677735

-- check how many distinct ip
select count(*) from (select distinct ip from log) as ipcount; -- 762

-- check how many distinct method
select count(*) from (select distinct method from log) as methodcount; -- 1

-- check what the method is
select * from (select distinct method from log) as methodcount; --GET

-- check how many distinct status code
select * from (select distinct status from log) as ipcount; -- 404 and 200

-- check how many distinct path in log
select count(*) from (select distinct path from log) as pathcount; -- 212

-- join articles and log to find most popular
--select * from articles as A join log as L on L.path like concat('%', A.slug);

-- create a view for articles and log join
create view  articlesAndLog as
	select A.title, count(L.id) as view
	from articles as A join log as L on L.path 
	like concat('%', A.slug) 
	where L.status like '200%' 
	group by A.title order by count(L.id) desc;

-- create a view for articles and authors
create view articelsAndAuthors as
	select ar.title, au.name 
	from articles as ar 
	join authors as au 
	on ar.author = au.id;

-- create a view for views of each authors
create view authorView as
	select A.title, au.name, count(L.id) as view
		from articles as A join log as L on L.path 
		like concat('%', A.slug) 
		join authors as au on A.author = au.id
		where L.status like '200%' 
		group by A.title, au.name order by count(L.id) desc;

-- create a view to count daily error request
create view dailyError as
	select count(id) as error, date_trunc('day', time) as date from log 
	where status like '404%'
	group by date_trunc('day', time);

-- create a view to count daily success request
create view dailySuccess as
	select count(id) as success, date_trunc('day', time) as date from log 
	where status like '200%'
	group by date_trunc('day', time);

-- -- create a view to count daily total request
create view dailyTotal as
	select count(id) as total, date_trunc('day', time) as date from log 
	group by date_trunc('day', time);

-- create a view for daily statistic
create view dailyStats as 
	select e.error, s.success, t.total, t.date 
	from dailyerror as e 
	join dailysuccess as s 
		on e.date = s.date 
	join dailytotal as t 
		on t.date = s.date