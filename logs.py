#!/usr/bin/env python
import psycopg2

DBNAME = "news"

def db_connect(database_name):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"
    sys.exit(1) 

def db_execute_query(query):
    db, c = db_connect(DBNAME)
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result

if __name__ == '__main__':
    get_popular_articles_query = "select * from articlesAndLog limit 3"
    get_popular_author_query = "select sum(view), name from authorview \
    group by name order by sum(view) desc"
    get_day_of_bad_reques_query = "select \
    (cast(error as real) / cast(total as real)) as rate, date \
    from dailystats \
    where (cast(error as real) / cast(total as real)) > 0.01"
    articles_result = db_execute_query(get_popular_articles_query)
    authors_result = db_execute_query(get_popular_author_query)
    request_result = db_execute_query(get_day_of_bad_reques_query)
    print "|--------------------title----------------------|----views----|"
    for article in articles_result:
        print "\t {} \t {}".format(article[0], article[1])
    print "|----views----|---------------author-----------------|"
    for author in authors_result:
        print "   {} \t {}".format(author[0], author[1])
    print "|--------rate-------|--------------date-------------|"
    for rate in request_result:
        print "    {} \t       {}".format(rate[0], rate[1])
