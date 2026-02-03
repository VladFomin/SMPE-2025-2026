import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("M2R-ParallelQuicksort/M2R ParallelQuicksort/scripts/data/vfomin_2025-11-06/all_values.csv")

plt.figure(figsize=(8, 5))

plt.plot(data["Size"], data["Sequential_avg"], marker="o", color="blue", label="Sequential")
plt.plot(data["Size"], data["Parallel_avg"], marker="o", color="red", label="Parallel")
plt.plot(data["Size"], data["Libc_avg"], marker="o", color="green", label="Libc")

plt.title("Execution Time vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Average Execution Time (seconds)")
plt.legend(title="Implementation")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("quicksort_results.png", dpi=300)
plt.show()

