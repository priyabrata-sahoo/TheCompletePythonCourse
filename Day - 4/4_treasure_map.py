row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


c = int(position[1]) 
d = int(position[0])

map[c-1][d-1] = "X"
print(f"{row1}\n{row2}\n{row3}")