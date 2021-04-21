import pandas as pd
import mysql.connector


def connect_db():
    # Connect to mysql server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="CoolMint77#$",
    )
    # Show Connection
    # print(mydb)

    # Create Cursor Instance
    cursor = mydb.cursor()

    create_database(cursor)
    create_table(cursor)
    update_table(cursor)


def create_database(cursor):
    # Create Database
    cursor.execute("CREATE DATABASE IF NOT EXISTS player_statistics")
    return


def create_table(cursor):
    # Create Table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS player_statistics.average_stats (playerId VARCHAR(10) PRIMARY KEY NOT NULL, "
        "firstName VARCHAR(30) NOT NULL, lastName VARCHAR(30) NOT NULL, teamId VARCHAR(10), pos VARCHAR(10), "
        "points DECIMAL , totReb DECIMAL, assists DECIMAL, steals DECIMAL, blocks DECIMAL, turnovers DECIMAL, "
        "fantasyPoints DECIMAL)")
    return


def delete_table(cursor):
    # Delete Table
    cursor.execute("DROP  TABLE player_statistics.average_stats")
    return


def update_table(cursor):
    delete_table(cursor)
    create_database(cursor)
    return

