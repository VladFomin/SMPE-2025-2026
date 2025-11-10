import re
import statistics
import csv

# Пути к файлам
input_file = "/home/vladfomin/M2R-ParallelQuicksort/M2R ParallelQuicksort/scripts/data/vfomin_2025-11-06/measurements_1550.txt"
averages_file = "/home/vladfomin/M2R-ParallelQuicksort/M2R ParallelQuicksort/scripts/data/vfomin_2025-11-06/averages.csv"
all_values_file = "/home/vladfomin/M2R-ParallelQuicksort/M2R ParallelQuicksort/scripts/data/vfomin_2025-11-06/all_values.csv"

# Регулярные выражения
size_pattern = re.compile(r"^Size: (\d+)")
seq_pattern = re.compile(r"Sequential quicksort took: ([\d.]+) sec")
par_pattern = re.compile(r"Parallel quicksort took: ([\d.]+) sec")
libc_pattern = re.compile(r"Built-in quicksort took: ([\d.]+) sec")

data = {}
size = None

# Чтение исходного файла
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if match := size_pattern.match(line):
            size = int(match.group(1))
            data.setdefault(size, {"seq": [], "par": [], "libc": []})
        elif match := seq_pattern.match(line):
            data[size]["seq"].append(float(match.group(1)))
        elif match := par_pattern.match(line):
            data[size]["par"].append(float(match.group(1)))
        elif match := libc_pattern.match(line):
            data[size]["libc"].append(float(match.group(1)))

# 1️⃣ CSV с усреднёнными результатами
with open(averages_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Size", "Sequential_avg", "Parallel_avg", "Libc_avg"])
    for size, times in sorted(data.items()):
        writer.writerow([
            size,
            statistics.mean(times["seq"]) if times["seq"] else None,
            statistics.mean(times["par"]) if times["par"] else None,
            statistics.mean(times["libc"]) if times["libc"] else None,
        ])

# 2️⃣ CSV со всеми измерениями
with open(all_values_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Size", "Type", "Time_sec"])
    for size, times in sorted(data.items()):
        for t in times["seq"]:
            writer.writerow([size, "Sequential", t])
        for t in times["par"]:
            writer.writerow([size, "Parallel", t])
        for t in times["libc"]:
            writer.writerow([size, "Libc", t])

print("✅ Готово! Созданы файлы:")
print(f"- {averages_file}")
print(f"- {all_values_file}")
