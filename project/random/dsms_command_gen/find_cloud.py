from azure.kusto.data.helpers import dataframe_from_result_table
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder

def read_file():
    data = open('E:/repos/neanders-repo/project/random/dsms_command_gen/paths.csv').read().splitlines()
    return data

cluster = "https://dsms.kusto.windows.net"
db = "dsms"

def execute_query(cluster: str, db: str, query: str):
    kcsb = KustoConnectionStringBuilder.with_az_cli_authentication(cluster)
    client = KustoClient(kcsb)
    response = client.execute(db, query)
    df = dataframe_from_result_table(response.primary_results[0])
    return df

def main():
    print("Starting Script")
    results_list = []
    data = read_file()
    for dsms_path in data:
        query = f'''
        KPI_Inv_ResourcesAll
        | where ObjectType =~ "AdHocSecret"
        | where Name startswith "/hardwareproxy-prod/adhocsecrets/"
        | where Name == "{dsms_path}"
        | summarize by Name, Cloud
        '''
        print("Running Kusto query: ", query)
        df = execute_query(cluster, db, query)
        results_list.append(list(zip(df.Name, df.Cloud)))
    print("********************************************")
    print("Script Finished")
    print("********************************************")
    print(results_list)

if __name__ == "__main__":
    main()