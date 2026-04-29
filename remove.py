import os, time
path = "/tmp" # Windows用 os.environ.get('TEMP')
now = time.time()
for f in os.listdir(path):
    p = os.path.join(path, f)
    if os.stat(p).st_mtime < now - 86400:
        print(f"清理: {f}")
        # os.remove(p) # 确认无误后取消注释
