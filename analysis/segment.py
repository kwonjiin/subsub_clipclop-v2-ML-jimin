# 세그먼트 분석

import pandas as pd
from sklearn.cluster import KMeans

def segment_analysis(df: pd.DataFrame, n_clusters: int = 3):
    """
    df: [user_id, watch_time, monthly_payment, genre_pref_score ...]
    """
    features = df.drop(columns=['user_id'])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['segment'] = kmeans.fit_predict(features)
    return df[['user_id', 'segment']]
