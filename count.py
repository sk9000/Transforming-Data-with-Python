import read
from collections import Counter
if __name__=="__main__":
    df = read.load_data()
    head = df["headline"]
    full_head = ""
    for h in head:
        full_head = full_head+str(h)
    lst = full_head.split(" ")
    dic = Counter(lst)
    print(dic.most_common(100))
        
        