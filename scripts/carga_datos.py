from pymongo import MongoClient

file = open('atp_tennis.csv', mode = 'r')

client = MongoClient()
db = client["tennisDb"]
collection = db["tournaments"]

atpTennis = file.readlines()


atpTennis = [line.split(',') for line in atpTennis]

dataToDatabase = []


print(atpTennis[0])
for data in atpTennis:
    documento = {
    atpTennis[0][0]: data[0],
    atpTennis[0][1]: data[1],
    atpTennis[0][2]: data[2],
    atpTennis[0][3]: data[3],
    atpTennis[0][4]: data[4],
    atpTennis[0][5]: data[5],
    atpTennis[0][6]: data[6],
    atpTennis[0][7]: data[7],
    atpTennis[0][8]: data[8],
    atpTennis[0][9]: data[9],
    atpTennis[0][10]: data[10],
    atpTennis[0][11]: data[11],
    atpTennis[0][12]: data[12],
    atpTennis[0][13]: data[13],
    atpTennis[0][14]: data[14],
    atpTennis[0][15]: data[15],
    atpTennis[0][16]: data[16],
}
    dataToDatabase.append(documento)
collection.insert_many(dataToDatabase)
    