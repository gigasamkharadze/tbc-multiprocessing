# JSON Fetcher with Multiprocessing and Multithreading

This Python application efficiently fetches data from multiple 
URLs by leveraging both multiprocessing and multithreading. It allows 
concurrent data retrieval, improving performance and responsiveness.


## Requirements

- Python 3.x
- Install the required dependencies using the provided requirements.txt file:

```bash
  pip install -r requirements.txt
```

## Usage

1. Clone or download the project repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the script using the following command:
```bash
python main.py
```
or
```bash
python3 main.py
```

### Customization
The script can be customized by modifying the following parameters in the `main.py` file:
1. `URLS`: A list of URLs to fetch data from.
2. `NUMBER_OF_PROCESSES` : The number of processes to use for concurrent data retrieval. default is 5.
3. `NUMBER_OF_THREADS_PER_PROCESS` : The number of threads to use for concurrent data retrieval. default is 20.

# Contributions

We welcome contributions to improve this project! Feel free to fork the repository and submit pull requests with your changes. Please ensure that any contributions align with the project's goals and adhere to the coding standards. For major changes, please open an issue first to discuss the proposed changes.