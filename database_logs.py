#!/usr/bin/ python3

import psycopg2

DBNAME = 'news'  # Database name
"""Query for the question "What are the \
    most popular three articles of all time?"""
first_question_query = "select * from three_most_popular_articles;"
"""Query for the question "Who are the most popular \
    article authors of all time?"""
second_question_query = "select * from popular_article_authors"
"""Query for the question "On which days did \
    more than 1% of requests lead to errors?"""
third_question_query = "select * from days_with_more_than_1_percent_errors;"


def query_logs():
    """This function connects to database and runs queries \
    to fetch the results."""
    try:
        # Connects to the database news
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()
        # Executes the query and stores the each fetched results
        cursor.execute(first_question_query)
        top_articles = cursor.fetchall()
        cursor.execute(second_question_query)
        popular_authors = cursor.fetchall()
        cursor.execute(third_question_query)
        days_with_error = cursor.fetchall()

        # Prints answer for first question
        print("\n*** Most popular three articles ***")
        for article in top_articles:
            print(""""{0}" -- {1} views""".format(article[0], article[1]))
        # Prints answer for second question
        print("\n*** Most Popular Article Authors of all time ***")
        for author in popular_authors:
            print("{0} -- {1} views".format(author[0], author[1]))
        # Prints answer for third question
        print("\n*** Days on which more than 1% of requests led to errors ***")
        for days in days_with_error:
            print("{0} -- {1}".format(days[0], days[1]))
    finally:
        db.close()  # close the database

query_logs()  # run the query_logs function
