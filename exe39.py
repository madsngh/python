'''lets start with directories'''
print("\'_\'"*10)
#lets make my 1st directory
sid={'age': '19','dob': '7 jan 1996','weight': '62','height': '70 inche','colour': 'fair'}
print(sid["age"])
del sid['age']
print(sid)
sid['dob']='7 jan 1994'
print(sid)
print(sid.get("weight"))
print(sid.keys())
print(sid.values())