from csv import writer


def csvgenerator(filename, csv_list):
    with open(filename + '.csv', 'w', newline='') as file:
        writer_object = writer(file)
        writer_object.writerow(["LINK ID", "URL", "RESPONSE CODE", "DOWNLOADED PATH", "DEPTH"])
        for i in csv_list:
            # print(i,csv_list[i],end="\n")
            writer_object.writerow(csv_list[i])
    file.close()
