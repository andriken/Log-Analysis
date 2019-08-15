#!/usr/bin/ python3

import psycopg2

DBNAME = 'news' # Database name

# Queries
top_articles_query = "select * from three_most_popular_articles;"
top_authors_query = "select * from popular_article_authors"
top_error_days_query = "select * from days_with_more_than_1_percent_errors;"


def fetch_query(query):
    """Connect to the database, query, fetch results,
    close connection"""
    results = None
    try:
        # Connects to the database news and grabs cursor
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()
        # Executes the query, fetch result and store into variable
        cursor.execute(query)
        results = cursor.fetchall()
    finally:
        # Close database and return result
        db.close()
        return results


def print_top_articles():
    """Fetch top articles using helper function"""

    top_articles = fetch_query(top_articles_query)
    print("\n*** Most popular three articles ***")
    for article in top_articles:
        print(""""{0}" -- {1} views""".format(article[0], article[1]))


def print_top_authors():
    """Fetch top authors using helper function"""

    popular_authors = fetch_query(top_authors_query)
    print("\n*** Most Popular Article Authors of all time ***")
    for author in popular_authors:
        print("{0} -- {1} views".format(author[0], author[1]))


def print_top_error_days():
    """Fetch top error days using helper function"""

    days_with_error = fetch_query(top_error_days_query)
    print("\n*** Days on which more than 1% of requests led to errors ***")
    for days in days_with_error:
        print("{0} -- {1}".format(days[0], days[1]))


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_top_error_days()
