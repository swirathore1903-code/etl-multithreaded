import queue

def extract_worker(input_queue, transform_queue):
    while not input_queue.empty():
        data = input_queue.get()
        transform_queue.put(data)
        input_queue.task_done()

def transform_worker(transform_queue, load_queue):
    while True:
        try:
            data = transform_queue.get(timeout=2)
            data['value'] = data['value'] * 2
            load_queue.put(data)
            transform_queue.task_done()
        except:
            break

def load_worker(load_queue, results):
    while True:
        try:
            data = load_queue.get(timeout=2)
            results.append(data)
            load_queue.task_done()
        except:
            break