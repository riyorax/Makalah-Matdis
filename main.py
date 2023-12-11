import sys

def dijkstra(graph, src):
    row = len(graph)
    dist = [sys.maxsize] * row
    dist[src] = 0
    visited = [False] * row

    for _ in range(row):
        u = min_distance(dist, visited)
        visited[u] = True

        for v in range(row):
            if graph[u][v] > 0 and visited[v] is False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist

def min_distance(dist, visited):
    min_val = sys.maxsize
    min_index = -1

    for v in range(len(dist)):
        if dist[v] < min_val and visited[v] is False:
            min_val = dist[v]
            min_index = v

    return min_index

petaParkirMobil = [
    [0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 228, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60],
    [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 138, 0, 0, 157, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 138, 0, 69, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 69, 0, 162, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 162, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 157, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 50, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 60, 0, 131, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 131, 0, 50, 0, 178, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 219, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 178, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 0, 90, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192],
    [228, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 219, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 136, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 136, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 112, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 112, 0, 0],
    [60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

petaParkirMotor = [
    [0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 228, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 138, 0, 0, 157, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 138, 0, 69, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0],
    [0, 0, 0, 69, 0, 162, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 162, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65, 0, 0, 0, 0, 0, 0],
    [0, 0, 157, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 50, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 60, 0, 131, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 131, 0, 50, 0, 178, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 219, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 178, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 0, 180],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 0],
    [228, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 219, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0, 0, 0, 0, 0, 0, 196, 0, 0, 0, 0, 0],
]

def ketersediaanSabuga(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 80
    elif 8 <= hour < 9:
        return 70
    elif 9 <= hour < 10:
        return 60
    elif 10 <= hour < 11:
        return 50
    elif 11 <= hour < 12:
        return 50
    elif 12 <= hour < 13:
        return 50
    elif 13 <= hour < 14:
        return 50
    elif 14 <= hour < 15:
        return 60
    elif 15 <= hour < 16:
        return 70
    elif 16 <= hour < 17:
        return 80
    elif 17 <= hour < 18:
        return 80

def ketersediaanBonbin(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 80
    elif 8 <= hour < 9:
        return 70
    elif 9 <= hour < 10:
        return 60
    elif 10 <= hour < 11:
        return 50
    elif 11 <= hour < 12:
        return 50
    elif 12 <= hour < 13:
        return 50
    elif 13 <= hour < 14:
        return 50
    elif 14 <= hour < 15:
        return 60
    elif 15 <= hour < 16:
        return 70
    elif 16 <= hour < 17:
        return 80
    elif 17 <= hour < 18:
        return 80

def ketersediaanTamfest(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 80
    elif 8 <= hour < 9:
        return 50
    elif 9 <= hour < 10:
        return 40
    elif 10 <= hour < 11:
        return 30
    elif 11 <= hour < 12:
        return 30
    elif 12 <= hour < 13:
        return 20
    elif 13 <= hour < 14:
        return 20
    elif 14 <= hour < 15:
        return 40
    elif 15 <= hour < 16:
        return 60
    elif 16 <= hour < 17:
        return 70
    elif 17 <= hour < 18:
        return 70

def ketersediaanSaraga(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 80
    elif 8 <= hour < 9:
        return 70
    elif 9 <= hour < 10:
        return 60
    elif 10 <= hour < 11:
        return 50
    elif 11 <= hour < 12:
        return 50
    elif 12 <= hour < 13:
        return 50
    elif 13 <= hour < 14:
        return 60
    elif 14 <= hour < 15:
        return 70
    elif 15 <= hour < 16:
        return 80
    elif 16 <= hour < 17:
        return 80
    elif 17 <= hour < 18:
        return 90
    
def ketersediaanSeniRupa(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 60
    elif 8 <= hour < 9:
        return 50
    elif 9 <= hour < 10:
        return 50
    elif 10 <= hour < 11:
        return 40
    elif 11 <= hour < 12:
        return 40
    elif 12 <= hour < 13:
        return 30
    elif 13 <= hour < 14:
        return 20
    elif 14 <= hour < 15:
        return 40
    elif 15 <= hour < 16:
        return 70
    elif 16 <= hour < 17:
        return 70
    elif 17 <= hour < 18:
        return 80
    
def ketersediaanSipil(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 60
    elif 8 <= hour < 9:
        return 50
    elif 9 <= hour < 10:
        return 50
    elif 10 <= hour < 11:
        return 50
    elif 11 <= hour < 12:
        return 40
    elif 12 <= hour < 13:
        return 30
    elif 13 <= hour < 14:
        return 20
    elif 14 <= hour < 15:
        return 40
    elif 15 <= hour < 16:
        return 70
    elif 16 <= hour < 17:
        return 80
    elif 17 <= hour < 18:
        return 80
    
def ketersediaanSkanda(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 80
    elif 8 <= hour < 9:
        return 50
    elif 9 <= hour < 10:
        return 40
    elif 10 <= hour < 11:
        return 30
    elif 11 <= hour < 12:
        return 30
    elif 12 <= hour < 13:
        return 20
    elif 13 <= hour < 14:
        return 20
    elif 14 <= hour < 15:
        return 40
    elif 15 <= hour < 16:
        return 60
    elif 16 <= hour < 17:
        return 50
    elif 17 <= hour < 18:
        return 70
    
def ketersediaanGelapNyawang(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 80
    elif 8 <= hour < 9:
        return 50
    elif 9 <= hour < 10:
        return 40
    elif 10 <= hour < 11:
        return 40
    elif 11 <= hour < 12:
        return 30
    elif 12 <= hour < 13:
        return 20
    elif 13 <= hour < 14:
        return 20
    elif 14 <= hour < 15:
        return 40
    elif 15 <= hour < 16:
        return 60
    elif 16 <= hour < 17:
        return 70
    elif 17 <= hour < 18:
        return 70
    
def ketersediaanCiungwanara(hour):
    if 6 <= hour < 7:
        return 100
    elif 7 <= hour < 8:
        return 80
    elif 8 <= hour < 9:
        return 50
    elif 9 <= hour < 10:
        return 40
    elif 10 <= hour < 11:
        return 30
    elif 11 <= hour < 12:
        return 30
    elif 12 <= hour < 13:
        return 20
    elif 13 <= hour < 14:
        return 20
    elif 14 <= hour < 15:
        return 40
    elif 15 <= hour < 16:
        return 60
    elif 16 <= hour < 17:
        return 70
    elif 17 <= hour < 18:
        return 70
    
def isGraphSym(graph):
    valid = True
    i = 0
    while i < 23 and valid:
        j = 0
        while j < 23 and valid:
            if graph[i][j] != graph[j][i]:
                valid = False
                print("Tidak simetris di ", i, j)
            else:
                j +=1
        i +=1
    if valid:
        print("GACOR KANG")

def idxKelas(n):
    if n == 1:
        return 14
    elif n == 2:
        return 16
    elif n == 3:
        return 17
    elif n == 4:
        return 19
    elif n == 5:
        return 20
    elif n == 6:
        return 21
    
def hargaSabugaMobil():
    return 10000

def hargaSabugaMotor():
    return 3000

def hargaSeniRupaMobil():
    return 10000

def hargaSeniRupaMotor():
    return 3000

def hargaSipilMotor():
    return 3000

def hargaSaragaMobil(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour*4000 < 9000:
        return totHour*4000
    else:
        return 9000

def hargaSaragaMotor(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour*2000 < 3000:
        return totHour*2000
    else:
        return 3000

def hargaTamfesMobil(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour<= 4:
        return 8000
    else:
        return 1000

def hargaTamfesMotor(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour<= 4:
        return 3000
    else:
        return 4000

def hargaCiungwanaraMobil(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour<= 1:
        return 5000
    elif totHour <= 4:
        return 10000
    else:
        return 15000

def hargaSkandaMobil(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour<= 1:
        return 5000
    elif totHour <= 4:
        return 10000
    else:
        return 15000

def hargaGanyangMobil(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour<= 1:
        return 5000
    else:
        return 10000

def hargaBonbinMobil(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour == 1:
        return 5000
    else:
        return (totHour-1)*4000 + 5000

def hargaBonbinMotor(hourIn, hourOut):
    totHour = hourOut-hourIn
    if totHour == 1:
        return 3000
    else:
        return (totHour-1)*2000 + 3000

def calcScore(distance, price, ketersediaan):
    return 3*ketersediaan + 2*(1/distance) + 1/price

print("===================PARKIR PICKER=====================")
jenis = input("Masukkan Jenis Kendaraan(Motor/Mobil): ")
while jenis != "mobil" and jenis != "Mobil" and jenis != "motor" and jenis != "Motor":
    print("Input antara motor dan mobil!")
    jenis = input("Masukkan Jenis Kendaraan(Motor/Mobil): ")
if jenis == "mobil" or jenis == "Mobil":

    print("1. Sabuga\n2. Oktagon\n3. TVST\n4. GKUB\n5. Labtek V\n6. GKUT")
    tempatParkMobil = int(input("Pilih Tempat Kelas(1-5): "))
    while tempatParkMobil < 1 or tempatParkMobil > 6:
        print("Input antara 1-6!")
        print("1. Sabuga\n2. Oktagon\n3. TVST\n4. GKUB\n5. Labtek V\n6. GKUT")
        tempatParkMobil = int(input("Pilih Tempat Kelas(1-5): "))

    jamParkir = int(input("Pilih Jam Parkir:"))
    while jamParkir < 6 or jamParkir >= 18:
        print("Input antara 6-17!")
        jamParkir = int(input("Pilih Jam Parkir:"))

    jamKeluar = int(input("Pilih Jam Keluar:"))
    while jamKeluar <= jamParkir or jamKeluar > 18:
        print("Input antara lebih besar dari jam parkir!")
        jamKeluar = int(input("Pilih Jam Keluar:"))

    
    idxMobil = idxKelas(tempatParkMobil)
    listDistance = dijkstra(petaParkirMobil, idxMobil)
    jarakSabuga = listDistance[13]
    jarakSaraga = listDistance[15]
    jarakBonbin = listDistance[18]
    jarakSeniRupa = listDistance[22]
    jarakCiungwanara = listDistance[23]
    jarakSkanda = listDistance[24]
    jarakGanyang = listDistance[25]
    jarakTamfes = listDistance[26]

    hargaSabuga = hargaSabugaMobil()
    hargaSaraga = hargaSaragaMobil(jamParkir, jamKeluar)
    hargaBonbin = hargaBonbinMobil(jamParkir, jamKeluar)
    hargaSeniRupa = hargaSeniRupaMobil()
    hargaCiungwanara = hargaCiungwanaraMobil(jamParkir, jamKeluar)
    hargaSkanda = hargaSkandaMobil(jamParkir, jamKeluar)
    hargaGanyang = hargaGanyangMobil(jamParkir, jamKeluar)
    hargaTamfes = hargaTamfesMobil(jamParkir, jamKeluar)

    availSabuga = ketersediaanSabuga(jamParkir)
    availSaraga = ketersediaanSaraga(jamParkir)
    availBonbin = ketersediaanBonbin(jamParkir)
    availSeniRupa = ketersediaanSeniRupa(jamParkir)
    availCiungwanara = ketersediaanCiungwanara(jamParkir)
    availSkanda = ketersediaanSkanda(jamParkir)
    availGanyang = ketersediaanGelapNyawang(jamParkir)
    availTamfes = ketersediaanTamfest(jamParkir)

    sabuga = calcScore(jarakSabuga, hargaSabuga, availSabuga)
    saraga = calcScore(jarakSaraga, hargaSaraga, availSaraga)
    bonbin = calcScore(jarakBonbin, hargaBonbin, availBonbin)
    seniRupa = calcScore(jarakSeniRupa, hargaSeniRupa, availSeniRupa)
    ciungwanara = calcScore(jarakCiungwanara, hargaCiungwanara, availCiungwanara)
    skanda = calcScore(jarakSkanda, hargaSkanda, availSkanda)
    ganyang = calcScore(jarakGanyang, hargaGanyang, availGanyang)
    tamfes = calcScore(jarakTamfes, hargaTamfes, availTamfes)

    bestParkScore = max(sabuga, saraga, bonbin, seniRupa, ciungwanara, skanda, ganyang, tamfes)
    parkingSpace = {
        sabuga: "Sabuga",
        saraga: "Saraga",
        bonbin: "Kebun Binatang",
        seniRupa: "Seni Rupa",
        ciungwanara: "Ciungwanara",
        skanda: "Skanda",
        ganyang: "Gelap Nyawang",
        tamfes: "Taman Festival"
    }

    bestLoc = parkingSpace[bestParkScore]

    print("Berdasarkan hasil perhitungan tempat terbaik adalah", bestLoc)

else:
    print("1. Sabuga\n2. Oktagon\n3. TVST\n4. GKUB\n5. Labtek V\n6. GKUT")
    tempatParkMotor = int(input("Pilih Tempat Kelas(1-5): "))
    while tempatParkMotor < 1 or tempatParkMotor > 6:
        print("1. Sabuga\n2. Oktagon\n3. TVST\n4. GKUB\n5. Labtek V\n6. GKUT")
        print("Input antara 1-6!")
        tempatParkMobil = int(input("Pilih Tempat Kelas(1-5): "))
        
    idxMotor = idxKelas(tempatParkMotor)
    listDistance = dijkstra(petaParkirMotor, idxMotor)

    jamParkir = int(input("Pilih Jam Parkir:"))
    while jamParkir < 6 or jamParkir >= 18:
        print("Input antara 6-17!")
        jamParkir = int(input("Pilih Jam Parkir:"))

    jamKeluar = int(input("Pilih Jam Keluar:"))
    while jamKeluar <= jamParkir or jamKeluar > 18:
        print("Input antara lebih besar dari jam parkir!")
        jamKeluar = int(input("Pilih Jam Keluar:"))

    jarakSabuga = listDistance[13]
    jarakSaraga = listDistance[15]
    jarakBonbin = listDistance[18]
    jarakSeniRupa = listDistance[22]
    jarakTamfes = listDistance[23]
    jarakSipil = listDistance[24]

    hargaSabuga = hargaSabugaMotor()
    hargaSaraga = hargaSaragaMotor(jamParkir, jamKeluar)
    hargaBonbin = hargaBonbinMotor(jamParkir, jamKeluar)
    hargaSeniRupa = hargaSeniRupaMotor()
    hargaTamfes = hargaTamfesMotor(jamParkir, jamKeluar)
    hargaSipil = hargaSipilMotor()

    availSabuga = ketersediaanSabuga(jamParkir)
    availSaraga = ketersediaanSaraga(jamParkir)
    availBonbin = ketersediaanBonbin(jamParkir)
    availSeniRupa = ketersediaanSeniRupa(jamParkir)
    availTamfes = ketersediaanTamfest(jamParkir)
    availSipil = ketersediaanSipil(jamParkir)

    sabuga = calcScore(jarakSabuga, hargaSabuga, availSabuga)
    saraga = calcScore(jarakSaraga, hargaSaraga, availSaraga)
    bonbin = calcScore(jarakBonbin, hargaBonbin, availBonbin)
    seniRupa = calcScore(jarakSeniRupa, hargaSeniRupa, availSeniRupa)
    tamfes = calcScore(jarakTamfes, hargaTamfes, availTamfes)
    sipil = calcScore(jarakSipil, hargaSipil, availSipil)

    bestParkScore = max(sabuga, saraga, bonbin, seniRupa, tamfes, sipil)
    parkingSpace = {
        sabuga: "Sabuga",
        saraga: "Saraga",
        bonbin: "Kebun Binatang",
        seniRupa: "Seni Rupa",
        tamfes: "Taman Festival",
        sipil: "Sipil"
    }

    bestLoc = parkingSpace[bestParkScore]
    print("Berdasarkan hasil perhitungan tempat terbaik adalah", bestLoc)
