""" Script to remove SDWAN files for Cisco ISR 4351 devices.
    Having these files on the device after upgrading to 17.3.2 will
    cause the device to go down.
"""

import logging
import re

import net_devices2
from net_devices2.drivers import CiscoBase
from net_task import app, read_write
from net_task.utilites import log_results_kusto

TASK_NAME = 'cisco_4351_remove_sdwan'

logger = logging.getLogger(__name__)

SHOW_BOOTFLASH_INSTALLER = "show bootflash: all | in installer"
DELETE_FILES = "delete /force bootflash:/{}"
DELETE_RECURSIVE_FILES = "delete /recursive /force bootflash:/{}"

def is_installer_file_present(handler):
    """ Check for /bootflash/.installer/active
    Args:
        handler (obj):
    Returns:
        (bool)
    """
    result = handler.connection.send_command(SHOW_BOOTFLASH_INSTALLER)
    return bool(re.search('bootflash/.installer/active', result))

@read_write
@app.task(bind=True)
def cisco_4351_remove_sdwan(self,
                            device_name,
                            read_write=True):
    """ Remove SDWAN files from bootflash on Cisco 4351s
        Args:
             device_name (str): device to update
             read_write (bool): mandatory arg for using the safe pipeline
    """
    handler = net_devices2.get_device_handler(device_name)
    handler.connect(read_write=read_write)

    #Verify Device is Cisco
    if not isinstance(handler, CiscoBase):
        logger.error('Unexpected OS. Only Cisco IOS-XE is supported')
        log_results_kusto(device_name, TASK_NAME, self.request.id, 'pre-check failure: unsupported os')
        return

    #Verify Hardware SKU is Cisco 4351
    if "4351" not in handler.hardware_sku:
        logger.error('Unexpected hardware sku. Only Cisco4351 is supported.')
        log_results_kusto(device_name, TASK_NAME, self.request.id, 'pre-check failure: unsupported sku')
        return

    #Check if files are present
    if is_installer_file_present(handler) == False:
        logger.error('Device does not match criteria for SDWAN file removal (Did not find "/bootflash/.installer/active" in flash')
        log_results_kusto(device_name, TASK_NAME, self.request.id, "workflow completed: no SDWAN files were found on the device")
        return

    #Remove files from device
    handler.connection.send_command(DELETE_RECURSIVE_FILES.format("sdwan"))
    handler.connection.send_command(DELETE_FILES.format(".installer/images/active"))
    handler.connection.send_command(DELETE_RECURSIVE_FILES.format(".installer"))
    handler.connection.send_command(DELETE_RECURSIVE_FILES.format(".sdwaninstallerfs"))
    handler.connection.send_command(DELETE_FILES.format(".sdwaninstaller/images/active"))
    handler.connection.send_command(DELETE_RECURSIVE_FILES.format(".sdwaninternal"))
    handler.connection.send_command(DELETE_RECURSIVE_FILES.format("vmanage-admin"))

    #Check if files are present post workflow
    if is_installer_file_present(handler) == False:
        log_results_kusto(device_name, TASK_NAME, self.request.id, "post-check failure: /bootflash/.installer/active still in flash")
        return

    log_results_kusto(device_name, TASK_NAME, self.request.id, "post-check success: SDWAN files removed")