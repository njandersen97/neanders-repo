import net_devices2
# from azure.kusto.data.helpers import dataframe_from_result_table
# from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from kusto_proxy.teams import PhyNetKustoProxy


cluster = "https://azphynet.kusto.windows.net/"
db = "azdhmds"
query = '''
DeviceStatic
| where Status == "InProduction"
| where Role !contains 'UnManaged'
| where StaticIP != "0.0.0.0" or ManagementIP != "0.0.0.0"
| where NgsDeviceType !contains 'epms'
| where HardwareSku !contains "digi"
| where NgsDeviceType !contains 'Optical'
| where Vender in ('Cisco', 'Arista')
| where OSVersion !contains "Sonic"
| project DeviceName
| take 10
'''
swan_query = '''
DeviceStatic
| where Status == "InProduction"
| where DeviceName contains "ibr"
| where Vender =~ "Cisco"
| project DeviceName
| take 10
'''


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

def test_auth_config(device):
    try:
        handler = net_devices2.get_device_handler(device)
        latest_passwords = handler.get_latest_passwords(use_dsms=True)
        ndm_config = handler.get_configlet("Authentication").lines
        auth_config = handler._get_local_auth_config_from_ndm(ndm_config, latest_passwords)
        print('Device: ',device,'| Config: ',auth_config)
    except Exception as e:
        print('Device: ',device,' hit an exception: ',e)


def main():
    print('Running Kusto query for standard device list')
    device_list = execute_query(cluster, db, query)
    print('Running Kusto query for swan device list')
    swan_device_list = execute_query(cluster, db, swan_query)
    print('Grabbing configs for standard device list')
    for device in device_list:
        test_auth_config(device)
    print('---------------------------------------------------')
    print('Grabbing configs for swan device list')
    for device in swan_device_list:
        test_auth_config(device)



if __name__ == "__main__":
    main()