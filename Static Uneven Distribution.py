import random

# jumlah task
tasks = []
for i in range(12):
    tasks.append(random.randint(1, 6))  # durasi random

# pembagian static (tidak merata dari awal)
w1 = tasks[0:4]
w2 = tasks[4:7]
w3 = tasks[7:10]
w4 = tasks[10:]

def kerja(nama, daftar_task):
    total = 0
    print("\n", nama)
    
    for i in range(len(daftar_task)):
        print("  task", i+1, "waktu:", daftar_task[i])
        total += daftar_task[i]
    
    print("  total waktu:", total)
    return total

# jalanin semua worker
t1 = kerja("Worker 1", w1)
t2 = kerja("Worker 2", w2)
t3 = kerja("Worker 3", w3)
t4 = kerja("Worker 4", w4)

# total sistem (yang paling lama)
total = max(t1, t2, t3, t4)

print("\nHasil akhir:")
print("Total waktu sistem:", total)

# cek sederhana apakah seimbang atau tidak
rata = (t1 + t2 + t3 + t4) / 4

print("Rata-rata:", rata)

print("\nSelisih tiap worker:")
print("W1:", abs(t1 - rata))
print("W2:", abs(t2 - rata))
print("W3:", abs(t3 - rata))
print("W4:", abs(t4 - rata))