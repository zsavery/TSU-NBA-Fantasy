import pymysql


def to_mysql(df):
    cert = {"host": "localhost",
            "port": 3306,
            "user": "admin",
            "passwd": "tigers"}

    conn = pymysql.connect(host=cert["host"],
                           port=cert["port"],
                           user=cert["user"],
                           passwd=cert["passwd"],
                           charset='utf8')
    database = "stats_test"
    # grant_privileges = f"grant all privileges on {cert['host']}.{database} to `{cert['user']}`@`localhost`;"
    # conn.cursor().execute(grant_privileges)
    conn.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    conn = pymysql.connect(host=cert["host"],
                           port=cert["port"],
                           user=cert["user"],
                           passwd=cert["passwd"],
                           db=database,
                           charset='utf8')
    table = "stats"
    create_table = f"""create table if not exists {database}.{table}(
        playerId INTEGER(8) unique not null,
        firstName varchar(30),
        lastName varchar(30),
        teamId INTEGER(8),
        pos varchar(10),
        points DECIMAL(5,2),
        totReb DECIMAL(5,2),
        assists DECIMAL(5,2),
        steals DECIMAL(5,2),
        blocks DECIMAL(5,2),
        turnovers DECIMAL(5,2),
        fantasyPoints DECIMAL(5,2), 
        primary key(playerId));"""
    conn.cursor().execute(create_table)
    for playerId, firstName, lastName, teamId, pos, points, totReb, assists, steals, blocks, turnovers, fantasyPoints \
            in zip(df['playerId'], df['firstName'], df['lastName'], df['teamId'], df['pos'], df['points'], df['totReb'],
                   df['assists'], df['steals'], df['blocks'], df['turnovers'], df['fantasyPoints']):
        if "'" in firstName:
            firstName = firstName.replace("'", "''")

        if "'" in lastName:
            lastName = lastName.replace("'", "''")

        query = (f"""
        REPLACE INTO {database}.{table} (playerId, firstName, lastName, teamId, pos, points,
            totReb, assists, steals, blocks, turnovers, fantasyPoints) VALUES
            ('{playerId}', '{firstName}', '{lastName}', '{teamId}', '{pos}', {points}, {totReb}, {assists}, {steals}, {blocks}, {turnovers}, {fantasyPoints});""")
        print(query)

        conn.cursor().execute(query)
        print(f"Add playerId: {playerId}")
        conn.commit()


def drop():
    cert = {"host": "localhost",
            "port": 3306,
            "user": "admin",
            "passwd": "tigers"}

    conn = pymysql.connect(host=cert["host"],
                           port=cert["port"],
                           user=cert["user"],
                           passwd=cert["passwd"],
                           charset='utf8')
    database = "stats_test"
    conn.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    conn = pymysql.connect(host=cert["host"],
                           port=cert["port"],
                           user=cert["user"],
                           passwd=cert["passwd"],
                           db=database,
                           charset='utf8')
    table = "stats"
    query = (f'''
    DROP TABLE IF EXISTS {database}.{table}
    ''')

    conn.cursor().execute(query)
    conn.commit()
