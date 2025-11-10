
library(ggplot2)

data <- read.csv("M2R-ParallelQuicksort/M2R ParallelQuicksort/scripts/data/vfomin_2025-11-06/measurements.csv")

ggplot(data, aes(x = Size)) +
  geom_line(aes(y = Sequential_avg, color = "Sequential")) +
  geom_line(aes(y = Parallel_avg, color = "Parallel")) +
  geom_line(aes(y = Libc_avg, color = "Libc")) +
  geom_point(aes(y = Sequential_avg, color = "Sequential")) +
  geom_point(aes(y = Parallel_avg, color = "Parallel")) +
  geom_point(aes(y = Libc_avg, color = "Libc")) +
  scale_color_manual(values = c("Sequential" = "blue", "Parallel" = "red", "Libc" = "green")) +
  labs(
    title = "Execution Time vs Array Size",
    x = "Array Size",
    y = "Average Execution Time (seconds)",
    color = "Implementation"
  ) +
  theme_minimal()
ggsave("quicksort_results.png", width = 7, height = 5)
