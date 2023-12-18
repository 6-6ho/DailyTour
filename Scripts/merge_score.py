import pandas as pd

def merge_score(review_type):
    file1_path = f'../Data/Predicted_Data/{review_type}_review_analysis_scores.csv'
    file2_path = f'../Data/Predicted_Data/{review_type}_review_avg_scores.csv'

    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    merged_df = pd.merge(df1, df2, on=f'{review_type}_NAME'.upper(), suffixes=('_df1', '_df2'))

    merged_df['SCORE'] = round((merged_df['SCORE_df1'] * 7 + merged_df['SCORE_df2'] * 3) / 10, 2)

    merged_df = merged_df[['CNT_NAME', 'REG_NAME', f'{review_type}_NAME'.upper(), f'{review_type}_REV_POS'.upper(), f'{review_type}_REV_NEG'.upper(), 'SCORE']]

    merged_df.to_csv(f'../Data/Predicted_Data/{review_type}_merged_score.csv', index=False)
    
    
if __name__=="__main__":
    review_types = ["accom", "attr"]
    for review_type in review_types:
        merge_score(review_type)

