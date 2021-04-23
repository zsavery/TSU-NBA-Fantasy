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
        playerId varchar(10) unique not null,
        firstName varchar(30),
        lastName varchar(30),
        teamId varchar(10),
        pos varchar(10),
        points DECIMAL,
        totReb DECIMAL,
        assists DECIMAL,
        steals DECIMAL,
        blocks DECIMAL,
        turnovers DECIMAL,
        fantasyPoints DECIMAL, 
        primary key(playerId));"""
    conn.cursor().execute(create_table)
    for playerId, firstName, lastName, teamId, pos, points, totReb, assists, steals, blocks, turnovers, fantasyPoints \
            in zip(df['playerId'], df['firstName'], df['lastName'], df['teamId'], df['pos'], df['points'], df['totReb'],
                   df['assists'], df['steals'], df['blocks'], df['turnovers'], df['fantasyPoints']):
        # query = ("INSERT INTO player_statistics.average_stats (playerId, firstName, lastName, teamId, pos, points, "
        #          "totReb, assists, steals, blocks, turnovers, fantasyPoints) VALUES "
        #          "(%s, %s, %s, %s, %s, %d, %d, %d, %d, %d, %)")
        # query = (f"""INSERT INTO {database}.{table} (playerId, firstName, lastName, teamId, pos, points,
        #                 totReb, assists, steals, blocks, turnovers, fantasyPoints) VALUES
        #                 (%s, %s, %s, %s, %s, %d, %d, %d, %d, %d, %d, %d)""")
        query = (f"""
        REPLACE INTO {database}.{table} (playerId, firstName, lastName, teamId, pos, points,
            totReb, assists, steals, blocks, turnovers, fantasyPoints) VALUES
            ('{playerId}', '{firstName}', '{lastName}', '{teamId}', '{pos}', {points}, {totReb}, {assists}, {steals}, {blocks}, {turnovers}, {fantasyPoints});""")
        print(query)
        # conn.cursor().execute(query, (playerId, firstName, lastName, teamId, pos, points, totReb, assists, steals,
        #                               blocks, turnovers, fantasyPoints,))
        conn.cursor().execute(query)
        print(f"Add playerId: {playerId}")
        conn.commit()

