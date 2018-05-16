import pandas as pd
from collections import Counter

def load_data():
    data = pd.read_csv("hn_stories.csv", names=["submission_time", "upvotes", "url", "headline"])
    return data

if __name__ == "__main__":
    data=load_data()
    string = ""
    for each in data["url"]:
        string = string + str(each) + " "
    lst = string.split(" ")
    dic = Counter(lst)
    print(dic.most_common(100))
                    
    