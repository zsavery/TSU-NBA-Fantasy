"""

"""
import pymysql


def to_mysql(df) -> None:
    """

    Args:
        df: A dataframe with twelve columns.

            {playerId: Numerical, firstName: String, lastName: String, teamId: Numerical, pos: Numerical,
            points: Numerical, totReb: Numerical, assists: Numerical, steals: Numerical, blocks: Numerical,
            turnovers: Numerical, fantasyPoints: Numerical}

    Returns:
        None

    """
    cert = {"host": "localhost",
            "port": 3306,
            "user": "admin",
            "passwd": "tigers"}

    # MySQL Connection
    conn = pymysql.connect(host=cert["host"],
                           port=cert["port"],
                           user=cert["user"],
                           passwd=cert["passwd"],
                           charset='utf8')
    database = "stats_test"

    # Create Database
    conn.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {database};")
    conn = pymysql.connect(host=cert["host"],
                           port=cert["port"],
                           user=cert["user"],
                           passwd=cert["passwd"],
                           db=database,
                           charset='utf8')
    table = "stats"

    # Create Table Based on Data Frame
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

    # Populate Table/Update Table
    for playerId, firstName, lastName, teamId, pos, points, totReb, assists, steals, blocks, turnovers, fantasyPoints \
            in zip(df['playerId'], df['firstName'], df['lastName'], df['teamId'], df['pos'], df['points'], df['totReb'],
                   df['assists'], df['steals'], df['blocks'], df['turnovers'], df['fantasyPoints']):
        if "'" in firstName:
            firstName = firstName.replace("'", "''")

        if "'" in lastName:
            lastName = lastName.replace("'", "''")

        update_table = f'''
        REPLACE INTO {database}.{table} (playerId, firstName, lastName, teamId, pos, points,
            totReb, assists, steals, blocks, turnovers, fantasyPoints) VALUES
            ('{playerId}', '{firstName}', '{lastName}', '{teamId}', '{pos}', {points}, {totReb}, {assists}, {steals},
             {blocks}, {turnovers}, {fantasyPoints});'''
        print(update_table)
        conn.cursor().execute(update_table)

        print(f"Add playerId: {playerId}")
    conn.commit()  # Ensures changes are made
    top5(conn, table)
    return


def top5(conn, table1) -> None:
    """
    Creates a _table_ in MySQL based on another table in the same database.
    Args:
        conn:
        table1:

    Returns:

    """
    table2 = "top5"
    n = 5
    selected_column = "fantasyPoints"

    drop_table(conn, table2)  #

    create_table2_like_table1 = f'''
    CREATE TABLE IF NOT EXISTS {table2} LIKE {table1};
    '''
    conn.cursor().execute(create_table2_like_table1)

    get_top_n_from_table1 = f'''
    INSERT {table2}
    SELECT *
    FROM {table1}
    ORDER BY {selected_column} DESC
    LIMIT {n};
    '''
    conn.cursor().execute(get_top_n_from_table1)
    conn.commit()
    return


def drop_table(conn, table) -> None:
    drop_table_query = (f'''
    DROP TABLE IF EXISTS {table}
    ''')
    conn.cursor().execute(drop_table_query)
    conn.commit()
    return
