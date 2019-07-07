import csv
with open ("data.csv" , 'w' , newline="") as fd:
    csv_write = csv.writer(fd, delimiter=',')
    csv_write.writerow(['Name', 'Age','Class'])
    csv_write.writerow(['Inam', 42 , 'AI'])
    csv_write.writerow(['Hamza' ,  30 , "AI"])