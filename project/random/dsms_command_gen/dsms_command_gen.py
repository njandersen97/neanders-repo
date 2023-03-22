from datetime import datetime

now = datetime.now()
currentMonth = now.strftime("%B")
currentYear = now.strftime("%Y")

GET_COMMAND = 'DSMSClient GetSecret -url:https://global-dsms.dsms.core.windows.net -name:{} -file:/Users/NEANDERS/"Work Folders"/Desktop/DsmsClient/DsmsClient/{}/{}.txt'

ROLLOVER_COMMAND = 'Dsmsclient -url:https://global-dsms.dsms.core.windows.net  -name:{} -file:/Users/NEANDERS/"Work Folders"/Desktop/DsmsClient/DsmsClient/{}/{}.txt -readasbytes:true -retainfileaftercreation:true Rollover'

def read_file():
    data = open('E:/repos/neanders-repo/project/random/dsms_command_gen/paths.csv').read().splitlines()
    return data

dsms_path = "/hardwareproxy-prod/adhocsecrets/localaccounts/autopilot/dell/localaccount/passwordhashes/admin"

def gen_folder_file(dsms_path):
    folder = currentMonth + currentYear
    file = dsms_path.replace("/", "_")
    return folder, file

def gen_command(command, dsms_path):
    folder, file = gen_folder_file(dsms_path)
    command = command.format(dsms_path, folder, file)
    return command

def create_command_file(commands):
    with open('E:/repos/neanders-repo/project/random/dsms_command_gen/commands.txt', 'w') as file:
        for command in commands:
            file.write("%s\n" % command)

def main():
    commands = []

    data = read_file()
    for dsms_path in data:
        commands.append('Commands for {}'.format(dsms_path))
        get_command = gen_command(GET_COMMAND, dsms_path)
        commands.append(get_command)
        rollover_command = gen_command(ROLLOVER_COMMAND, dsms_path)
        commands.append(rollover_command)
        commands.append('\n')

    create_command_file(commands)
    print('Done')



if __name__ == "__main__":
    main()