import yaml

"""
This script was designed for the Networking-Device-Health repo

This scripts takes the config-base, checks for all repair scenarios lower than 3 (sev2s, sev1s), 
and inserts a severity override in the config-ussec file

The alerting config for the different clouds is configured to use default to config-base.yml,
but prioritize any config in the config-{cloudtype}.yml for the specific cloud. By using 
this script, you insert "Severity": 3 for any sev 2s or sev1s in the config, overriding the
base config

NOTE: This script removes comments from the YAML file, and does weird things to certain strings
within quotes
"""

# Key Value pair to be inserted
upd_sev = {"Severity": 3}

# Recursive loop to find Severity key in nested dictionaries
def find(d, sev):
    if sev in d:
        yield d[sev]
    for k, v in d.items():
        if isinstance(v, dict):
            for i in find(v, sev):
                yield i, k


# Open base config file to check for alerts configured sev 2 or lower
config_base = open(
    r"C:\Networking-Device-Health\src\GreenSeerServices\GSHAutoRepair\serviceconfig\config-base.yml",
    encoding="UTF-8",
)
base_data = yaml.load(config_base, Loader=yaml.FullLoader)

# Open ussec config file to insert severity override
config_ussec = open(
    r"C:\Networking-Device-Health\src\GreenSeerServices\GSHAutoRepair\serviceconfig\config-ussec.yml",
    encoding="UTF-8",
)
ussec_data = yaml.load(config_ussec, Loader=yaml.FullLoader)

high_sev_alert = ()

# Logic to look for any repair scenarios in the base config, check if severity is < 3
# and insert new severity to cloud config
for val in find(base_data, "Severity"):
    if val[0][0][0] < 3:
        high_sev_alert = val[0][1]
        for key in ussec_data["RepairScenarios"]:
            if key in high_sev_alert:
                # print(key+" needs to be overridden")
                ussec_data["RepairScenarios"][key]["IncidentTemplate"].update(upd_sev)
                with open("ussec_data", "w", encoding="UTF-8") as update_ussec_data:
                    yaml.dump(
                        ussec_data,
                        update_ussec_data,
                        default_flow_style=False,
                        sort_keys=False,
                    )
