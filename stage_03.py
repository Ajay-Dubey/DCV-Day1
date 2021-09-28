with open("Artifacts.txt","r") as f:
    text = f.read()
    print(text)

with open("Artifacts01.txt","w") as f:
    text = f.write(text + "new added line")
    print("End of stage_03")