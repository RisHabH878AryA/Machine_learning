# Read a csv, count number of rows, columns, missing vlaues.
with open("dataBook.csv", "r") as f:
    lines = f.readlines()
    
row_count = len(lines) - 1

columns = lines[0].strip().split(",")
col_count = len(columns)
print("columns: ", columns)
missing = 0

column_no = {0: "name", 1: "age", 2: "score"}

for line in lines:
    cells = line.strip().split(",")
    for cel_col in range(cells.__len__()):
        if(cells[cel_col].strip() == ""):
            missing += 1
            print(f'{column_no[cel_col]} missing in {cells}')

print("missing cell: ", missing)