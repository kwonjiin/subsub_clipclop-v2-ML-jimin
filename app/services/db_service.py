# 외부 DB 연결

import pandas as pd
from sqlalchemy import create_engine

# 예시: MySQL
DB_USER = "beyond"
DB_PASSWORD = "beyond"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "dagudok"

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def fetch_customer_data():
    query = """
    SELECT 
        user_id,
        signup_date,
        last_active_date,
        watch_time,
        monthly_payment,
        genre_pref_score,
        churn_flag
    FROM customer
    """
    df = pd.read_sql(query, engine)
    return df
