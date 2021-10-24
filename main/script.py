
import pandas as pd

def zeroOrAlt(l):
	allZero = True
	sign = -1
	alt = True
	for e in l:
		if e != 0:
			allZero = False
		if sign == -1:
			sign = (e >= 0)
		elif sign == (e >= 0):
			alt = False
		sign = (e >= 0)	
	return allZero or alt
	
def createDTable(table):
	till = len(table["y"])
	col = table["y"]
	prevCol = "y"
	order = 1
	while till and not zeroOrAlt(col):
		col = []
		
		for i in range(0, till-1):
			col.append(table[prevCol][i+1] - table[prevCol][i])
		table[f"∆y{order}"] = col
		order += 1
		prevCol = f"∆y{order-1}"
		till -= 1
	print("\nForeward Differences")
	print(pd.DataFrame.from_dict(table, orient = "index").T)
	print("Order observed is", order -2)

input("Make sure to have a file named 'xy.txt' in current directory")
opened = True
try:
	file = open("xy.txt", "r")
except Exception:
	opened = False
	print("File not found")	
if opened:
	table = {"x" : [], "y" : []}
	for line in file:
		table["x"].append([float(x) for x in line.split()][0])
		table["y"].append([float(x) for x in line.split()][1])
	createDTable(table)
	
	
	
	
