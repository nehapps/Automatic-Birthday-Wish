import pandas as pd
import datetime

def sendEmail(to, sub, msg):
  print(f"Email to {to} sent with subject: {sub} and  massage {msg}")
    


if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    # print(df)
    today =datetime.datetime.now().strftime("%d-%m")
    #print(today)

    for index, item in df.iterrows():
        #print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        print(bday)
        if(today == bday) & yearNow not in str(item['Year']):
            sendEmail(today, "Happy Birthday", item['Dialogue'])
            writeInd.append(index)
    #print(writeInd)        
    for i in writeInd:
        yr = def.loc[i,"Year"]
        df.loc[i, "Year"] = str(yr) + ','+str(yearNow)
        #print(df.loc[i,'year'])
        
    
   #print(df)
  df.to_excel('data.xlsx', index=False)
    

    
      
