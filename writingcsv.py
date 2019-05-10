import csv

with open('mycsv.csv','a') as f:
    fieldnames = ['columm1','columm2','columm3']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    a=input("Digite o seu a: ")
    thewriter.writerow({'columm1':a,'columm3':'three','columm2':'two'})
