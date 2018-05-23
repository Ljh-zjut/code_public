import csv
with open(r'C:\Users\小光\Desktop\中控实习\强化学习复现\20180313\green_occ20180313.csv',encoding=
'utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    n  =  149441
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    for i,rows in enumerate(csv_reader):
        if (i <= n-16 and i > n-24)or(i <= n-52 and i > n-56):
            m1 = float(rows[5])
            t1 = (m1*3600)/(float(rows[8])+4)
            t1 = int(t1)
            n1 = max(t1,n1)
        elif (i <= n and i > n-8)or(i <= n-32 and i > n-36):
            m2 = float(rows[5])
            t2 = (m2*3600)/(float(rows[8])+4)
            t2 = int(t2)
            n2 = max(t2,n2)
        elif(i <= n-56 and i > n-60)or(i <=  n-24 and i > n-28):
            m3 = float(rows[5])
            t3 = (m3*3600)/(float(rows[8])+4)
            t3 = int(t3)
            n3 = max(t3,n3)
        elif(i <= n-36 and i > n-44)or(i <= n-8 and i > n-12):
            m4 = float(rows[5])
            t4 = (m4*3600)/(float(rows[8])+4)
            t4 = int(t4)
            n4 = max(t4,n4)
    s1 = [n1,n2,n3,n4]
    print(s1)