import pymysql

def execute(c, command):
    c.execute(command)
    return c.fetchall()

db = pymysql.connect(host='localhost', user='root', passwd='yourpassword', db='chembl_24') #, charset='utf8')

c = db.cursor()

def export():
    file1 = open("sch.txt","r+")
    lines = file1.readlines()
    for line in lines:
        line = line.replace('\n',' ')
        line = line.strip()
        line = line.split(' ')
        for table in execute(c, "show tables;"):
            if line[0] == table[0]:
                line.pop(0)
                print line
                data1=""
                for j in line:
                    data1 = data1 + j+", "
                print data1
                data = execute(c, "select " + data1[:-2] + " from " + table[0] + ";")
                print data
                with open(table[0] + ".csv", "w") as out:
                    out.write("\t".join(line) + "\n")
                    for row in data:
                        out.write("\t".join(str(el) for el in row) + "\n")
                    print(table[0] + ".csv written")

export()

