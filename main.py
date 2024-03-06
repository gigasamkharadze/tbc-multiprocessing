import concurrent.futures
import json
import requests
import time

URL = 'https://dummyjson.com/products/'
NUMBER_OF_PROCESSES = 5
NUMBER_OF_THREADS_PER_PROCESS = 20


def get_data(i):
    try:
        response = requests.get(URL + str(i))
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from URL: {URL + str(i)}: {e}")
    else:
        return response.json()


def task_for_each_process(_):
    global NUMBER_OF_THREADS_PER_PROCESS
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUMBER_OF_THREADS_PER_PROCESS) as executor:
        product_data = list(executor.map(get_data, range(1, NUMBER_OF_THREADS_PER_PROCESS + 1)))
    return product_data


def main():
    global NUMBER_OF_PROCESSES
    with concurrent.futures.ProcessPoolExecutor(max_workers=NUMBER_OF_PROCESSES) as executor:
        data = list(executor.map(task_for_each_process, range(1, NUMBER_OF_PROCESSES + 1)))

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'Time taken: {end - start:.2f}')
