import re
import timeit

FAILBACK_REGEX = re.compile(r"%PLACEHOLDER:failback:\w*%", re.IGNORECASE)
test_failback_regex = r"%PLACEHOLDER:failback.+?%"
test2_failback_regex = r"%PLACEHOLDER:failback:[^%]*%"
control = r"%PLACEHOLDER:failback:FactoryDefault.NCS%"
FAILBACK_PWD_PLACEHOLDER = '$Secrets.FailbackPassword'

ndm_config = 'username failback secret 0 %PLACEHOLDER:failback:FactoryDefault.NCS%'

config = re.sub(FAILBACK_REGEX, FAILBACK_PWD_PLACEHOLDER, ndm_config)
print(config)

test_config = re.sub(test_failback_regex, FAILBACK_PWD_PLACEHOLDER, ndm_config)
print(test_config)

test2_config = re.sub(test2_failback_regex, FAILBACK_PWD_PLACEHOLDER, ndm_config)
print(test2_config)

control_config = re.sub(control, FAILBACK_PWD_PLACEHOLDER, ndm_config)
print(control_config)

# def regex1():
#     re.sub(test_failback_regex, FAILBACK_PWD_PLACEHOLDER, ndm_config)

# def regex2():
#     re.sub(test2_failback_regex, FAILBACK_PWD_PLACEHOLDER, ndm_config)

# def main():
#     regex1_execution_time = timeit.timeit(regex1, number=10000)
#     print(f"First Regex Execution time: {regex1_execution_time}")
#     regex2_execution_time = timeit.timeit(regex2, number=10000)
#     print(f"Second Regex Execution time: {regex2_execution_time}")


    
# if __name__ == "__main__":
#     main()