numberOfEntries = int(input())
addressBook = {}
for entry in range(numberOfEntries):
    inputFromUser = list(map(str,input().split()))
    addressBook[inputFromUser[0]] = inputFromUser[1]
inputs = []
while True:
    try:
        inp = input()
        inputs.append(inp)
    except:
        break
for name in inputs:
    if name in addressBook:
        print(name + "="+ str(addressBook[name])) 
    else:
        print("Not found")
