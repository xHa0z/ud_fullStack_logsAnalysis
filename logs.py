import psycopg2

DBNAME = "news"

def get_popular_articles():
	db = psycopg2.connect(database=DBNAME)
	cursor = db.cursor()
	cursor.execute("select * from articlesAndLog limit 3")
	result = cursor.fetchall()
	db.close()
	print result

def get_popular_author():
	db = psycopg2.connect(database=DBNAME)
	cursor = db.cursor()
	cursor.execute("select sum(view), name from authorview \
		group by name order by sum(view) desc")
	result = cursor.fetchall()
	db.close()
	print result

def get_day_of_bad_reques():
	db = psycopg2.connect(database=DBNAME)
	cursor = db.cursor()
	cursor.execute("select \
		(cast(error as real) / cast(total as real)) as rate, date \
		from dailystats \
		where (cast(error as real) / cast(total as real)) > 0.01")
	result = cursor.fetchall()
	db.close()
	print result

if __name__ == '__main__':
	get_popular_articles()
	get_popular_author()
	get_day_of_bad_reques()