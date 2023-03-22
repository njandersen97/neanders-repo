def _get_password_hashes():
    """ Return the current password hash for a given username

        Args:
            connection (obj)
            username (str)

        Returns
            pw_hash (dict)
    """
    deployment = 3

    admin_result = """
    username admin password 5 $1$1HbktXVy$jOVs4GNsr3.DUgHG8.IYq1 role network-admin\n
    username failback password 5 ! role network-admin\n
    snmp-server user admin network-admin auth md5 test priv test localizedkey\n
    snmp-server user failback network-admin auth md5 test priv test localizedkey
    """

    enable_result = ""

    admin_lines = [line.strip() for line in admin_result.splitlines() if
                    line.strip().startswith("username")]
    enable_lines = [line.strip() for line in enable_result.splitlines() if
                    line.strip().startswith("enable secret")]
    print(admin_lines)
    print(enable_lines)

    # Only include lines with password or secret
    admin_lines = [line for line in admin_lines if "password" in line or "secret" in line]
    enable_lines = [line for line in enable_lines if "password" in line or "secret" in line]

    print(admin_lines)
    print(enable_lines)

    pw_hash = {"{} admin".format(deployment): None,
                "{} enable".format(deployment): None,
                "{} failback".format(deployment): None,
                }

    print(pw_hash)

    try:
        if admin_lines:
            for line in admin_lines:
                if line.startswith("username admin"):
                    print("Line starts with admin")

                    if "$1$" in line or "$5$" in line or "$6$" in line:
                        print(line)
                        pw_hash['{} admin'.format(deployment)] = [word for word in line.split() if
                                                                    word.startswith("$1$") or word.startswith(
                                                                        "$5$") or word.startswith("$6$")][0]
                        print(pw_hash)
                    elif "password 7" in line or "secret 4" in line:
                        pw_hash['{} admin'.format(deployment)] = line.split()[-1]

                    else:
                        # Hash does not meet the expected format
                        pw_hash['{} admin'.format(deployment)] = None

                elif line.startswith("username failback"):
                    if "$1$" in line or "$5$" in line or "$6$" in line:
                        pw_hash['{} failback'.format(deployment)] = [word for word in line.split() if
                                                                    word.startswith("$1$") or word.startswith(
                                                                        "$5$") or word.startswith("$6$")][0]
                    else:
                        # Hash does not meet the expected format
                        pw_hash['{} failback'.format(deployment)] = None

            print('test', pw_hash)
        if enable_lines:
            print('We hit enable')
            for line in enable_lines:

                if "$1$" in line or "$5$" in line or "$6$" in line:
                    pw_hash['{} enable'.format(deployment)] = [word for word in line.split() if
                                                                word.startswith("$1$") or word.startswith(
                                                                    "$5$") or word.startswith("$6$")][0]
                elif "password 7" in line or "secret 4" in line:
                    pw_hash['{} enable'.format(deployment)] = line.split()[-1]
                print(pw_hash)
    except Exception as e:
        print(
            "Unhandled exception in output parsing {}: {}, {}".format(e, admin_lines,
                                                                            enable_lines))
        return None
    print('Great success')
    return pw_hash

def main():
    pw_hash = _get_password_hashes()
    print(pw_hash)



if __name__ == "__main__":
    main()