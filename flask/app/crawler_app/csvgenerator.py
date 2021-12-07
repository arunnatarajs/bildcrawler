from csv import writer


def csvgenerator(filename, csv_list):
    with open(filename + '.csv', 'w', newline='') as file:                                          #opening file to write
        writer_object = writer(file)                                                                #creating object to write in csv file
        writer_object.writerow(["LINK ID", "URL", "RESPONSE CODE", "DOWNLOADED PATH", "DEPTH"])     # providing heading to each columns
        for i in csv_list:
            # print(i,csv_list[i],end="\n")
            writer_object.writerow(csv_list[i])                                                     #writing each link in each row
    file.close()                                                                                    #closing file after writing
