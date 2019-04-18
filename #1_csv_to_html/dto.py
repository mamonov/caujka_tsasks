import csv

with open('C2ImportUsersSample.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',', quotechar='|')
    table_data = rows
    strTable = "<html><table>"

    for idx, row in enumerate(rows):
        strRW = "<tr>"
        for cell in row:
            strCell = "<td>" + cell + "</td>"
            strRW = strRW + strCell
        strRW = strRW + "</tr>"
        strTable = strTable + strRW

    strTable = strTable + "</table></html>"

    hs = open("asciiCharHTMLTable.html", 'w')
    hs.write(strTable)

    print(strTable)

    # for row in rows:
    #     print(', '.join(row))
