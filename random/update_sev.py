import yaml
import sys
from yaml.loader import FullLoader


def find(d, sev):
    if sev in d:
        yield d[sev]
    for k, v in d.items():
        if isinstance(v, dict):
            for i in find(v, sev):
                yield i, k

config_base = open(r"C:\Networking-Device-Health\src\GreenSeerServices\GSHAutoRepair\serviceconfig\config-base.yml")
base_data = yaml.load(config_base, Loader=yaml.FullLoader)

config_ussec = open(r"C:\Networking-Device-Health\src\GreenSeerServices\GSHAutoRepair\serviceconfig\config-ussec.yml")
# config_ussec = open(r"C:\neanders-repo\random\test.yml")
ussec_data = yaml.load(config_ussec, Loader=yaml.FullLoader)

high_sev_alert = ()

for val in find(base_data, 'Severity'):
    if val[0][0][0] < 3:
        high_sev_alert = val[0][1]
        for key in ussec_data["RepairScenarios"]:
            if key in high_sev_alert:
                print(key+" needs to be overridden")

