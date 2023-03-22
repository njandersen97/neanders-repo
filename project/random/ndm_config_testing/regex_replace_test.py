import re

ADMIN_PWD_PLACEHOLDER = '$Secrets.AdminPassword'
ENABLE_PWD_PLACEHOLDER = '$Secrets.EnableSecret'
FAILBACK_PWD_PLACEHOLDER = '$Secrets.FailbackPassword'
SWANAGENT1_PWD_PLACEHOLDER = '$Secrets.SwanAgent1Password'
SWANAGENT2_PWD_PLACEHOLDER = '$Secrets.SwanAgent2Password'
ROOT_PWD_PLACEHOLDER = '$Secrets.RootPassword'

ndm_config = ['username failback', 'username failback group root-lr', 'username failback group serviceadmin', 'username failback group cisco-support',
                'username failback secret 0 %PLACEHOLDER:failback:FactoryDefault.NCS%', 'username _swanagent1', 'username _swanagent1 group read-only-tg',
                'username _swanagent1 secret 0 %PLACEHOLDER:_swanagent1:FactoryDefault.NCS%', 'username _swanagent2', 'username _swanagent2 group read-only-tg',
                'username _swanagent2 secret 0 %PLACEHOLDER:_swanagent2:FactoryDefault.NCS%']

latest_passwords = {'failback': 'failbackpassword', '_swanagent1': '_swanagent1password', '_swanagent2': '_swanagent2password'}

def _get_local_auth_config_from_ndm(ndm_config, latest_passwords):
    accounts = ["admin",
                "[eE]nable",
                "failback",
                '_swanagent1',
                '_swanagent2',
                "root"]

    def _compile_account_regex(account):
        return re.compile(f"%PLACEHOLDER:{account}:\w*%".format(account), re.IGNORECASE)

    (ADMIN_REGEX,
        ENABLE_REGEX,
        FAILBACK_REGEX,
        SWANAGENT1_REGEX,
        SWANAGENT2_REGEX,
        ROOT_REGEX) = [_compile_account_regex(account) for account in accounts]

    FAILBACK_REGEX = r'%PLACEHOLDER:failback:\w*%'

    print('Printing regex______________________________________________________________________')
    print('__________________________________________________________________________________________')
    print(ADMIN_REGEX)
    print(ENABLE_REGEX)
    print(FAILBACK_REGEX)
    print(SWANAGENT1_REGEX)
    print(SWANAGENT2_REGEX)
    print(ROOT_REGEX)
    print('__________________________________________________________________________________________')

    config = "\n".join([line.strip() for line in ndm_config])
    print('Printing config after strip_______________________________________________________________________')
    print('__________________________________________________________________________________________')
    print(config)
    print('__________________________________________________________________________________________')
    config = re.sub(ADMIN_REGEX, ADMIN_PWD_PLACEHOLDER, config)
    config = re.sub(ENABLE_REGEX, ENABLE_PWD_PLACEHOLDER, config)
    config = re.sub(FAILBACK_REGEX, FAILBACK_PWD_PLACEHOLDER, config)
    config = re.sub(SWANAGENT1_REGEX, SWANAGENT1_PWD_PLACEHOLDER, config)
    config = re.sub(SWANAGENT2_REGEX, SWANAGENT2_PWD_PLACEHOLDER, config)
    config = re.sub(ROOT_REGEX, ROOT_PWD_PLACEHOLDER, config)

    print('Printing config after regex sub_______________________________________________________________________')
    print('__________________________________________________________________________________________')
    print(config)
    print('__________________________________________________________________________________________')

    (admin_pwd,
        enable_pwd,
        failback_pwd,
        swanagent1_pwd,
        swanagent2_pwd,
        root_pwd) = [latest_passwords.get(account) for account in ['admin',
                                                                'enable',
                                                                'failback',
                                                                '_swanagent1',
                                                                '_swanagent2',
                                                                'root']]

    config_lines = config.splitlines()
    output = []
    for line in config_lines:
        if ADMIN_PWD_PLACEHOLDER in line and admin_pwd:
            output.append(line.replace(ADMIN_PWD_PLACEHOLDER, admin_pwd))
        if ENABLE_PWD_PLACEHOLDER in line and enable_pwd:
            output.append(line.replace(ENABLE_PWD_PLACEHOLDER, enable_pwd))
        if FAILBACK_PWD_PLACEHOLDER in line and failback_pwd:
            output.append(line.replace(FAILBACK_PWD_PLACEHOLDER, failback_pwd))
        if SWANAGENT1_PWD_PLACEHOLDER in line and swanagent1_pwd:
            output.append(line.replace(SWANAGENT1_PWD_PLACEHOLDER, swanagent1_pwd))
        if SWANAGENT2_PWD_PLACEHOLDER in line and swanagent2_pwd:
            output.append(line.replace(SWANAGENT2_PWD_PLACEHOLDER, swanagent2_pwd))
        if ROOT_PWD_PLACEHOLDER in line and root_pwd:
            output.append(line.replace(ROOT_PWD_PLACEHOLDER, root_pwd))
        if 'PLACEHOLDER' not in line.upper() and '$SECRETS' not in line.upper() and not line.upper().lstrip() \
                .startswith('NO '):  # Remove un-replaced placeholder and secerts and delete command
            output.append(line)

    return "\n".join(output)


# def _og_get_local_auth_config_from_ndm(ndm_config, latest_passwords):
#     ADMIN_REGEX = re.compile(r"%PLACEHOLDER:admin:\w*%", re.IGNORECASE)
#     ENABLE_REGEX = re.compile(r"%PLACEHOLDER:[eE]nable:\w*%", re.IGNORECASE)
#     FAILBACK_REGEX = re.compile(r"%PLACEHOLDER:failback:\w*%", re.IGNORECASE)
#     ROOT_REGEX = re.compile(r"%PLACEHOLDER:root:\w*%", re.IGNORECASE)
#     config = None

#     admin_pwd = latest_passwords.get('admin')
#     enable_pwd = latest_passwords.get('enable')
#     failback_pwd = latest_passwords.get('failback')
#     root_pwd = latest_passwords.get('root')
#     config = "\n".join([line.strip() for line in ndm_config])
#     config = re.sub(ADMIN_REGEX, ADMIN_PWD_PLACEHOLDER, config)
#     config = re.sub(ENABLE_REGEX, ENABLE_PWD_PLACEHOLDER, config)
#     config = re.sub(FAILBACK_REGEX, FAILBACK_PWD_PLACEHOLDER, config)
#     config = re.sub(ROOT_REGEX, ROOT_PWD_PLACEHOLDER, config)

#     config_lines = config.splitlines()
#     output = []
#     for line in config_lines:
#         if ADMIN_PWD_PLACEHOLDER in line and admin_pwd:
#             output.append(line.replace(ADMIN_PWD_PLACEHOLDER, admin_pwd))
#         if ENABLE_PWD_PLACEHOLDER in line and enable_pwd:
#             output.append(line.replace(ENABLE_PWD_PLACEHOLDER, enable_pwd))
#         if FAILBACK_PWD_PLACEHOLDER in line and failback_pwd:
#             output.append(line.replace(FAILBACK_PWD_PLACEHOLDER, failback_pwd))
#         if ROOT_PWD_PLACEHOLDER in line and root_pwd:
#             output.append(line.replace(ROOT_PWD_PLACEHOLDER, root_pwd))
#         if 'PLACEHOLDER' not in line.upper() and '$SECRETS' not in line.upper() and not line.upper().lstrip() \
#                 .startswith('NO '):  # Remove un-replaced placeholder and secerts and delete command
#             output.append(line)

#     return "\n".join(output)

auth_config = _get_local_auth_config_from_ndm(ndm_config, latest_passwords)
print('Printing final config_________________________________________________________________________')
print('__________________________________________________________________________________________')
print(auth_config)
print('__________________________________________________________________________________________')

# og_auth_config = _og_get_local_auth_config_from_ndm(ndm_config, latest_passwords)
# print('Printing original final config_________________________________________________________________________')
# print('__________________________________________________________________________________________')
# print(og_auth_config)
# print('__________________________________________________________________________________________')

def test_regex():
    accounts = ["admin",
                "[eE]nable",
                "failback",
                '_swanagent1',
                '_swanagent2',
                "root"]

    def _compile_account_regex(account):
        return re.compile(rf'%PLACEHOLDER:{account}:\w*%', re.IGNORECASE)

    config = ndm_config

    (ADMIN_REGEX,
        ENABLE_REGEX,
        FAILBACK_REGEX,
        SWANAGENT1_REGEX,
        SWANAGENT2_REGEX,
        ROOT_REGEX) = [_compile_account_regex(account) for account in accounts]

    print(FAILBACK_REGEX)
    config = re.sub(FAILBACK_REGEX, FAILBACK_PWD_PLACEHOLDER, config)
    print(config)

# print(test_regex_
# This gives re.compile('%PLACEHOLDER:failback:\\w*%', re.IGNORECASE)
# It should give re.compile('%PLACEHOLDER:failback:\w*%', re.IGNORECASE)