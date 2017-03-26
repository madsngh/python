def findStrings(a, query):
    s=[]
    a=list(set(a))
    for word in a:
        for i in range(word.__len__()):
           for count in range(i,word.__len__()+1):
               k=word[i:count]
               if k!='':
                   if not (k in s ):
                       s.append(k)
    s.sort()
    for num in query:
        try:
            print(s[num-1])
        except:
            print("INVALID")


if __name__ == '__main__':
    n = int(input())
    string = []
    for i in range(0, n):
        string.append(input().strip())
    q = int(input())
    query = []
    for i in range(0, q):
        t1 = int(input())
        query.append(t1)
    findStrings(string, query)