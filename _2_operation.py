import json
import os

def register(filename,name,mobile_no,email_ID,password):
    details = {
        "Full Name":name,
        "Mobile Number":mobile_no,
        "Email ID":email_ID,
        "Password":password
    }

    file = open(filename,"r+")

    try:
        data=json.load(file)
        if details not in data:
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst = []
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    return False

def login(filename,email_ID,Password):
    file=open(filename,"r")
    try:
        data=json.load(file)
        for i in data:
            if i["Email ID"]==email_ID and i["Password"]==Password:
                return True
            else:
                return False
    except json.decoder.JSONDecodeError:
        return False
    finally:
        file.close()
    return False

def create_module(filename,module_id,module_name,start_date,end_date):
    details={
        "module_id":module_id,
        "module_name":module_name,
        "start_date":start_date,
        "end_date":end_date
    }
    if os.path.exists(filename)==False:
        file=open(filename,"x")
        print("file got created")
    else:
        print("file already exist")
        file=open(filename,"r+")
    try:
        data=json.load(file)
        if details not in data:
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    return False

def module_view(filename):
    file_data=None
    with open(filename) as file:
        file_data=json.load(file)
    return file_data

def delete_module(filename,module_id):
    with open(filename,"r+") as file:
        file_data=json.load(file)
        for i in range(len(file_data)):
            if file_data[i]["module_id"]==module_id:
                file_data.pop(i)
                file.seek(0)
                file.truncate()
                json.dump(file_data,file)
                file.close()
                return True
    return False

def update_module(filename,module_id,module_name,start_date,end_date):
    with open(filename,"r+") as file:
        file_data=json.load(file)
        for i in range(len(file_data)):
            if file_data[i]["module_id"]==module_id:
                file_data[i]["module_name"]==module_name
                file_data[i]["start_date"]==start_date
                file_data[i]["end_date"]==end_date
                file.seek(0)
                file.truncate()
                json.dump(file_data,file)
                return True
    return False

 

            

