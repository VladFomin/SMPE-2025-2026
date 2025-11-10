import pandas as pd
import matplotlib.pyplot as plt

# Загружаем CSV
data = pd.read_csv("M2R-ParallelQuicksort/M2R ParallelQuicksort/scripts/data/vfomin_2025-11-06/all_values.csv")

# Создаём фигуру
plt.figure(figsize=(8, 5))

# Линии с точками
plt.plot(data["Size"], data["Sequential_avg"], marker="o", color="blue", label="Sequential")
plt.plot(data["Size"], data["Parallel_avg"], marker="o", color="red", label="Parallel")
plt.plot(data["Size"], data["Libc_avg"], marker="o", color="green", label="Libc")

# Подписи и стиль
plt.title("Execution Time vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Average Execution Time (seconds)")
plt.legend(title="Implementation")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Сохраняем график
plt.savefig("quicksort_results.png", dpi=300)
plt.show()
