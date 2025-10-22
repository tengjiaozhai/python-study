# 运维系统命令 类似Liunx
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())

print(psutil.disk_partitions())
print(psutil.disk_io_counters())
print(psutil.net_io_counters())
