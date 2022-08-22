import net_devices2
# from azure.kusto.data.helpers import dataframe_from_result_table
# from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from kusto_proxy.teams import PhyNetKustoProxy


cluster = "https://azphynet.kusto.windows.net/"
db = "azdhmds"
query = '''
DeviceStatic
| where HardwareSku in ('Arista-7804-WAN-Generic', 'Arista-7816-WAN-Generic', 'Arista-7808-WAN-Generic')
| project DeviceName
'''


# def execute_query(cluster: str, db: str, query: str):
#     kcsb = KustoConnectionStringBuilder.with_az_cli_authentication(cluster)
#     client = KustoClient(kcsb)
#     # construct query and execute
#     print(f"Executing following query on database {db} on cluster {client._kusto_cluster}:\n{query}")
#     response = client.execute(db, query)
#     df = dataframe_from_result_table(response.primary_results[0])
#     device_list = df.iloc[:, 0].values.tolist()
#     return device_list

def execute_query(cluster: str, db: str, query: str):
    device_list = []
    try:
        kusto_client = PhyNetKustoProxy(kusto_cluster=cluster)
        response = kusto_client.execute_query(db, query)
        for device in response.fetchall():
            device_list.append(device['DeviceName'])
        return device_list

    except Exception:
        print("Exception in running Kusto Query, please run again")


def main():
    device_list = execute_query(cluster, db, query)
    for device in device_list:
        handler = net_devices2.get_device_handler(device)
        dsms_secret = handler.get_latest_passwords(use_dsms=True)
        print('Device: ',device,'| Secrets: ',dsms_secret)


if __name__ == "__main__":
    main()