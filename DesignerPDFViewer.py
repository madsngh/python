h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip(" ")
l=word.split(" ")
Total_max=0
for wrd in l:
    wrd = [(ord(eve) % 97) for eve in wrd]
    max = 0
    for no in wrd:
        if(max<h[no]):
            max=h[no]
    Total_max=Total_max+max*len(wrd)
print(Total_max)







'''Total_max=0
for wrd in l:
        wrd=[(ord(eve)%97) for eve in wrd]
        print(wrd)
        max=0
        for ele in range(0,len(wrd)):
            print("comparing",h[ele],max,ele)
            if(h[ele]>max):
                max=h[ele]
        print(max)
        Total_max=Total_max+max*len(wrd)
print(Total_max)'''
'''
6 3 4 4 6 4 5 3 4 3 6 5 4 6 7 1 3 4 2 5 6 1 5 1 7 2
nrdyluacvr
'''
'''6



'''