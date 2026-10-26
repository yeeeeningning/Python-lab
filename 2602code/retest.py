import time

n = 100000
items = list(range(n))
# 构造一个查询列表（包含存在于不存在的情况）
queries = [0, n // 2, n - 1, n] 

# --- 1. 测量构造集合的耗时 ---
start = time.perf_counter()
members = set(items)
build_seconds = time.perf_counter() - start

# --- 2. 测量列表查询的耗时 ---
list_times = []
for _ in range(3): # 测三次
    start = time.perf_counter()
    for _ in range(100): # 重复多轮，避免单次太快误差大
        for target in queries:
            target in items
    list_times.append(time.perf_counter() - start)

# --- 3. 测量集合查询的耗时 ---
set_times = []
for _ in range(3): # 测三次
    start = time.perf_counter()
    for _ in range(100): # 同样重复100轮
        for target in queries:
            target in members
    set_times.append(time.perf_counter() - start)

# --- 4. 打印结果 (计时区间外打印) ---
print(f"【构造集合耗时】: {build_seconds} 秒\n")
print(f"【列表查询耗时】(3次):")
for t in list_times: print(f"  {t} 秒")
print(f"【集合查询耗时】(3次):")
for t in set_times: print(f"  {t} 秒")