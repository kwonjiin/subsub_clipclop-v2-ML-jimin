# 코호트 분석 

import pandas as pd

def cohort_analysis(df: pd.DataFrame):
    """
    df: [user_id, signup_date, last_active_date]
    """
    df['signup_month'] = pd.to_datetime(df['signup_date']).dt.to_period('M')
    df['last_active_month'] = pd.to_datetime(df['last_active_date']).dt.to_period('M')

    # 각 사용자별 첫 가입 Cohort
    cohorts = df.groupby('user_id')['signup_month'].min().reset_index()
    df = df.merge(cohorts, on='user_id', suffixes=('', '_cohort'))

    # Cohort별 잔존율 계산
    cohort_pivot = df.groupby(['signup_month_cohort', 'last_active_month']).agg({'user_id':'nunique'}).reset_index()
    cohort_pivot = cohort_pivot.pivot(index='signup_month_cohort', columns='last_active_month', values='user_id').fillna(0)
    
    cohort_size = cohort_pivot.iloc[:,0]
    retention = cohort_pivot.divide(cohort_size, axis=0).round(3)
    
    return retention