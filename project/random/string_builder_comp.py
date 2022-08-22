import argparse
import timeit

parser = argparse.ArgumentParser()
parser.add_argument('--device_names', type=str,
                    help='list of device names')
args = parser.parse_args()


def nelsons_func():
    device_list = args.device_names.split(",")
    Content = "', '".join(device_list)
    finalContent = "('" + Content + "')"
    return finalContent
    # print(finalContent)


def matthews_func():
    device_tuple = '(\'' + args.device_names.replace(',', '\', \'') + '\')'
    return device_tuple
    # print(device_tuple)


def nigels_func():
    kusto_str = str(tuple(args.device_names.split(",")))
    return kusto_str
    # print(kusto_str)


def main():
    nelsons_execution_time = timeit.timeit(nelsons_func, number=10000)
    print(f"Nelson's Execution time: {nelsons_execution_time}")
    matthews_execution_time = timeit.timeit(matthews_func, number=10000)
    print(f"Matthew's Execution time: {matthews_execution_time}")
    nigels_execution_time = timeit.timeit(nigels_func, number=10000)
    print(f"Nigels's Execution time: {nigels_execution_time}")

    
if __name__ == "__main__":
    main()