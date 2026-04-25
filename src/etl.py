import pandas as pd
import threading
import queue
from src.workers import extract_worker, transform_worker, load_worker

def run_etl(num_threads):
    df = pd.read_csv("data/input.csv")

    input_queue = queue.Queue()
    transform_queue = queue.Queue()
    load_queue = queue.Queue()

    for _, row in df.iterrows():
        input_queue.put(row.copy())

    results = []
    threads = []

    # Extract threads
    for _ in range(num_threads):
        t = threading.Thread(target=extract_worker, args=(input_queue, transform_queue))
        t.start()
        threads.append(t)

    # Transform threads
    for _ in range(num_threads):
        t = threading.Thread(target=transform_worker, args=(transform_queue, load_queue))
        t.start()
        threads.append(t)

    # Load threads
    for _ in range(num_threads):
        t = threading.Thread(target=load_worker, args=(load_queue, results))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    result_df = pd.DataFrame(results)
    result_df.to_csv("output/result.csv", index=False)

    return result_df