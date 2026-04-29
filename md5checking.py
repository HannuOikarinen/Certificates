import hashlib

def md5sum(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

print(md5sum("ca.crt"))