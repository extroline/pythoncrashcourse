f = open("example.txt", "w")
f.write("Hello\n Meow")
f.close()

#f = open("example.txt", "a")
#f.write("Hello!!!")
#f.close()

f = open("example.txt", "r")
content = f.read()
print(content.split("\n"))
f.close()

#with open("example.txt", "w") as f:
 #   f.write("This is the last one! I promise!")