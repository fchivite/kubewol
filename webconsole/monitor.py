from concurrent.futures import ProcessPoolExecutor
import time


def execute_monitor(endpoint):
    print(f"Hello {endpoint['hostname']}")
    with ProcessPoolExecutor() as executor:
        resp = executor.map(endpoint_monitor, endpoint)
    return resp


def endpoint_monitor(endpoint):
    while True:
        time.sleep(endpoint['heartbeat'])
        print(endpoint['hostname'])