"""
1.Open file
2.Loop through lines assigning values into a new dic
3.Append each dict to a list
4.Return list
--------
5.Pass returned list + output filename into new Save function
6.Create a new output dict with key = "data" and value = passed in list
7.Output to json file
"""
import json

def save(filename, data):
    output_dict = {}
    output_dict["data"] = data
    
    with open(filename, 'w') as file_object:
        json.dump(output_dict, file_object, indent=2)

def readcurrency(filename):
    with open(filename, 'r') as file_object:
        output_list = []
        for line in file_object:
            line = line.replace("\n", "")           
            
            ccy_dict = {}
            ccy_dict["symbol"] = line.split()[0]
            ccy_dict["rate"] = float(line.split()[-1])

            output_list.append(ccy_dict)
    #return output_list
    #print(output_list)
    save("currency.json", output_list)

readcurrency("currency.txt")




