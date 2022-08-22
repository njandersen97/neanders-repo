from apscheduler.schedulers.blocking import BlockingScheduler
from azure.kusto.data.helpers import dataframe_from_result_table
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from decouple import config
from twilio.rest import Client


cluster = "https://phynetval.kusto.windows.net"
db = "NetworkValidationServiceLog"
query = '''
let deviceRegex = @"(?i)Device: (\S+)";
LogDebug
| where log contains "Message: Task failed due to PostSafetyChecker or snapshot comparison failed. Aborting."
| extend device = extract(deviceRegex, 1, log)
| project TIMESTAMP, device, log
| order by TIMESTAMP desc
| where TIMESTAMP > ago(12h)
'''

def execute_query(cluster: str, db: str, query: str):
    kcsb = KustoConnectionStringBuilder.with_az_cli_authentication(cluster)
    client = KustoClient(kcsb)
    response = client.execute(db, query)
    df = dataframe_from_result_table(response.primary_results[0])
    return df

def df_to_dict(df):
    df_list = list(zip(df.device, df.TIMESTAMP, df.log))
    df_dict = {}
    for (key, value1, value2) in df_list:
        if key in df_dict:
            df_dict[key].append(value1, value2)
        else:
            df_dict[key] = [value1, value2]
    return df_dict

account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN')
client = Client(account_sid, auth_token)

def main():
    df = execute_query(cluster, db, query)
    # print(df)
    # df_dict = df_to_dict(df)
    # print(df_dict)
    if not df.empty:
        client.messages.create(to="+15093895223", 
                       from_="+12136423074", 
                       body="There was a post SCS failure within the last hour")
        print('There was a post SCS failure within the last 30 minutes')
    else:
        print('DataFrame is empty indicating no post SCS failures within the last 30 minutes')

if __name__ == "__main__":
    main()
scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', minutes=30)
scheduler.start()