import csv

def problem_4(file_name):

    code = []
    avg_fine_dust = []
    ozone = []
    avg_ultrafine_dust = []

    with open('seoul_december_air.csv','r',encoding='euc-kr') as file:
        csv_data = csv.reader(file)

        for row in csv_data:
            group = row[3].strip()
            code.append(group)
        del code[0]

        for row in csv_data:
            group = row[5].strip()
            avg_fine_dust.append(group)
        del avg_fine_dust[0]
        
        for row in csv_data:
            group = row[6].strip()
            ozone.append(group)
        del ozone[0]

        for row in csv_data:
            group = row[7].strip()
            avg_ultrafine_dust.append(group)
        del avg_ultrafine_dust[0]

    value = list(map(list.__add__, avg_fine_dust, ozone, avg_ultrafine_dust))

    dict = dict(zip(code, value))


