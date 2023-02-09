# tagsThatWork = {'INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAM', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE'}

# file = "gedcomdata_input.ged"



# with open(file, "r") as gedfile:
#     for line in gedfile:
#         #print("--> " + line.strip())
#         parts = line.strip().split()
#         level = parts[0]
#         tag = parts[1]
#         args = " ".join(parts[2:]) if len(parts) > 2 else "" #this line is needed to handle arguments with multiple words
#         if (level == "0" and (args == "INDI" or args == "FAM")): #this line covers the exception
#             valid = "Y"
#             temp = tag
#             tag = args
#             args = temp
#         elif ((tag == "DATE" or tag == "Name") and args == ""): #this line covers the exception
#             valid = "N"
#         elif (tag in tagsThatWork):
#             valid = "Y"
#         else:
#             valid = "N"
#         print("<-- " + level + "|" + tag + "|" + valid + "|" + args)


class Individual:
    def __init__(self):
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

class Family:
    def __init__(self):
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

tagsThatWork = {'INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAM', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE'}

file = "gedcomdata_input.ged"

individuals = []
families = []

with open(file, "r") as gedfile:
    for line in gedfile:
        parts = line.strip().split()
        level = parts[0]
        tag = parts[1]
        args = " ".join(parts[2:]) if len(parts) > 2 else ""
        if (level == "0" and (args == "INDI" or args == "FAM")):
            valid = "Y"
            temp = tag
            tag = args
            args = temp
            
        elif ((tag == "DATE" or tag == "Name") and args == ""):
            valid = "N"
        elif (tag in tagsThatWork):
            valid = "Y"
        else:
            valid = "N"

        indi = Individual()
        fam = Family()

        # Add the line to the appropriate individual or family object
        if args == "INDI":
            indi.add_line(line)
        elif args == "FAM":
            fam.add_line(line)

#print the length of the individuals and families lists
print(len(individuals))
print(len(families))
