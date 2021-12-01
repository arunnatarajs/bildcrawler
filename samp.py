
from pandas import read_csv
def update_csv(url,rescode,path):
    df = read_csv("G:/vs_code_projects/crawler/www_kct_ac_in.csv")
    
    # updating the column value/data
    # df[:,"https://www.fleetstudio.com/labs",'RESPONSE CODE'] =200
    df.loc[df["URL"]==url.strip(),['RESPONSE CODE','DOWNLOADED PATH']] = [rescode,path]
    # df.loc[df["URL"]==url, 'DOWNLOADED PATH']
    df.to_csv("G:/vs_code_projects/crawler/www_kct_ac_in.csv",index=False)
    print(df)
