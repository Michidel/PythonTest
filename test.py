import time
import statistics
import sys

def solutie1(x, y):
    if x >= y:
        return "Ambele sunt egale"
    else:
        return "X este mai mare" if x > y else "Y este mai mare"

def solutie2(x, y):
    if x > y:
        return "X este mai mare"
    elif x < y:
        return "Y este mai mare"
    else:
        return "Ambele sunt egale"

# Seturi de date
inputs_equal = [(i, i) for i in range(1, 21)]
inputs_x_gt_y = [(i+1, i) for i in range(1, 21)]
inputs_y_gt_x = [(i, i+1) for i in range(1, 21)]
all_inputs = inputs_equal + inputs_x_gt_y + inputs_y_gt_x

def print_progress(percent, bar_len=40):
    filled = int(bar_len * percent // 100)
    bar = "#" * filled + "-" * (bar_len - filled)
    sys.stdout.write(f"\r[{bar}] {percent}%")
    sys.stdout.flush()

def run_bench(func, inputs, N=1_000_000):
    start = time.perf_counter()
    total = len(inputs) * N
    checkpoint = total // 100  # progres la fiecare 1%
    count = 0
    next_update = checkpoint
    for _ in range(N):
        for x, y in inputs:
            func(x, y)
            count += 1
            if count >= next_update:
                percent = (count * 100) // total
                print_progress(percent)
                next_update += checkpoint
    end = time.perf_counter()
    print_progress(100)
    print()  
    return end - start

# Benchmark cu progres
repeat = 3  # rulează de 3 ori pentru a calcula medie și deviație standard
times1, times2 = [], []

print("Rulez Solutia 1...")
for _ in range(repeat):
    times1.append(run_bench(solutie1, all_inputs, N=1_000_000))

print("Rulez Solutia 2...")
for _ in range(repeat):
    times2.append(run_bench(solutie2, all_inputs, N=1_000_000))

# Rezultate
avg1, std1 = statistics.mean(times1), statistics.stdev(times1)
avg2, std2 = statistics.mean(times2), statistics.stdev(times2)

print("\nRezultate finale:")
print(f"Soluția 1: media = {avg1:.6f}s, std = {std1:.6f}")
print(f"Soluția 2: media = {avg2:.6f}s, std = {std2:.6f}")

if avg1 < avg2:
    print(" Cea mai rapidă în medie este: Soluția 1")
elif avg2 < avg1:
    print(" Cea mai rapidă în medie este: Soluția 2")
else:
    print(" Ambele soluții sunt la fel de rapide în medie")