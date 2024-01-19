from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Picachu","Charmeleon", "Ledyba"])
table.add_column("Type", ["Electric", "Fire", "Bug Flying"])

table.align = "l"

print(table)
