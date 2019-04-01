# Log Analysis

Log Analysis Is a single file based python script that connects to database and logs the answers to three questions using **postgresql** queries.

### The Questions are as follows:
  1. _What are the most popular three articles of all time?_
  2. _Who are the most popular article authors of all time?_
  3. _On which days did more than 1% of requests lead to errors?_

### Requirements
This script runs on _**python 3**_
you'll need to install python library called **[Psycopg2](https://pypi.org/project/psycopg2/)**

# Documentation
The Postgresql queries used In the Python script are views based, you'll be required to run the each views commands listed below.
##### Postgresql Views:-
1.)
```
create view three_most_popular_articles as select title, count(log.path) as num 
from (select *, CONCAT('/article/', articles.slug) as slug_for_join from articles) as atfj left join log
on slug_for_join = log.path
group by title
order by num desc
limit 3;
```
2.)
```
create view popular_article_authors as select authors.name, count(log.path) as num 
from authors join (select *, CONCAT('/article/', articles.slug) as slug_for_join from articles) as atfj on authors.id = atfj.author 
left join log on atfj.slug_for_join = log.path
group by authors.name
order by num desc;
```
3.)
```
create view days_with_more_than_1_percent_errors as select s.d_day, concat(trunc(((fail::decimal / success) * 100.0), 2), '%') as p_of_error
from (select to_char(date_trunc('day', time), 'Mon dd, yyyy') as d_day, count(*) as success from log
where status = '200 OK' 
group by 1
order by 1) as s 
join (select to_char(date_trunc('day', time), 'Mon dd, yyyy') as d_day, count(*) as fail from log
where status = '404 NOT FOUND' 
group by 1
order by 1) as e
on s.d_day = e.d_day
where ((fail::decimal / success) * 100.0) > 2;
```

### Usage
After creating the views In the database, run the below command.
##### Command Line

```sh
$  python3 database_logs.py
```




