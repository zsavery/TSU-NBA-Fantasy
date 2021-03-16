from datetime import datetime

def get_season() -> str: 
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    season = ""

    if current_month == 12 and current_day >= 22:
        season = str(current_year) + '-' + str(current_year + 1)[2:]
    else:
        season = str(current_year - 1) + '-' + str(current_year)[2:]

    return season