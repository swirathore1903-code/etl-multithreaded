import time
from src.etl import run_etl
import matplotlib.pyplot as plt

threads_list = [1,2,3,4,5,6,7,8]
times = []

for t in threads_list:
    start = time.time()
    run_etl(t)
    end = time.time()

    time_taken = end - start
    times.append(time_taken)

    print(f"Threads: {t}, Time: {time_taken:.4f} sec")

plt.plot(threads_list, times, marker='o')
plt.xlabel("Number of Threads")
plt.ylabel("Execution Time (seconds)")
plt.title("Multi-threaded ETL Performance")
plt.savefig("output/performance.png")
plt.show()