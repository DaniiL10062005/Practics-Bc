import hashlib

def merge_Hash(arr, i, j, count_l, levels): 
    if len(arr) == 1:
        hash = hashlib.sha256(arr[0].encode()).hexdigest()
        return hash, count_l, levels
    if len(arr) % 2 != 0:
        arr.append(arr[-1])
        count_l+=1
    merged = []
    while j < len(arr):
        merged_item = (hashlib.sha256(arr[i].encode()).hexdigest()) + (hashlib.sha256(arr[j].encode()).hexdigest())
        merged.append(merged_item)
        i += 2
        j += 2
    return merge_Hash(merged, 0, 1, count_l, levels + 1) 


strings = ["abc", "5+5", "2*2", "666"]
hash, count, level = merge_Hash(strings, 0, 1, len(strings), 1)
print(hash, count, level)