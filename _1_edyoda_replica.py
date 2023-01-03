import re
from _2_operation import *
import random
if __name__=="__main__":
    while True:
        try:
            choice=int(input("enter\n1.Register\n2.Login\n3.Exit\n"))
        except ValueError:
            print("please enter valid choice 1-3!")
            continue
        if choice==1:
            try:
                register_choice=int(input("\n1.Register as Admin\n2.Register as studen\n3.exit\n"))
            except ValueError:
                print("please enter valid choce b/w 1-3!")
                continue

            if register_choice==1:
                name=input("enter your name:")
                mobile_no=input("enter your mobile number:")
                email=input("enter your email:")
                password=input("enter your password:")

                name_re=re.findall(r"^[A-Za-z]+$",name)
                mobile_no_re=re.findall(r"^[1-9]{1}/d{9}$",mobile_no)
                email_re=re.findall(r"^\w[@][a-z]+[.]com$",email)
                password_re=re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%*?&!])[A-Za-z\d@#$%^&*?]{6,16}",password)

                if name_re or mobile_no_re or email_re or password_re:
                    register_flag=register("admin_details.json",name,mobile_no,email,password)
                    if register_flag:
                        print("successfully registered")
                    else:
                        print("some thing went wrong")
                else:
                    if not name_re:
                        print("enter the name format correct ")
                        continue
                    if not mobile_no:
                        print("enter the mobile format correct")
                        continue
                    if not email:
                        print("enter the email format correct")
                        continue
                    if not password:
                        print("enter the password format correct")
                        continue
            if register_choice==2:
                print("Register as student:\n")
                name=input("enter a name:")
                mobile_no=int(input("enter a mobile number: "))
                email_ID1=input("enter a gmail:")
                Password=input("enter a password:")

                name_re=re.findall(r"^[A-Za-z]+$",name)
                mobile_no_re=re.findall(r"^[1-9]{1}/d{9}$",mobile_no)
                email_re=re.findall(r"^\w[@][a-z]+[.]com$",email)
                password_re=re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%*?&!])[A-Za-z\d@#$%^&*?]{6,16}",password)

                if name_re and mobile_no_re and email_re and Password:
                    register_flag=register("student_details.json",name,mobile_no,email,Password)
                    if register_flag:
                        print("Sucessfull")
                    else:
                        print("something went wrong")
                else:
                    if not name_re:
                        print("enter the name in correct format")
                    if not mobile_no_re:
                        print("enter the mobile_no in correct format")
                    if not email_re:
                        print("enter the email in correct format")
                    if not Password:
                        print("enter a password in correct format ")
                        continue
            if register_choice==3:
                exit()

        if choice==2:
            try:
                login_choice=int(input("\n1.login as Admin\n2.login as Student\n3.exit\n"))
            except:
                print("enter the login choice 1-3!")
                continue
            if login_choice==1:
                email=input("enter a email:")
                Password=input("enter a password:")
                login_flag=login("admin_details.json",email,Password)
                if login_flag:
                    print("login sucessfully")
                    while True:
                        try:
                            module_choice=int(input("\n1.create_module\n2.view_module\n3.update_module\n4.delete_module\n5.exit\n"))
                        except ValueError:
                            print("enter the choice b/w 1-5!")
                            continue
                        if module_choice==1:
                            module_id=random.randint(10000,20000)
                            module_name=input("enter a module name:")
                            start_date=input("enter start date yyyy-mm-dd:")
                            end_date=input("enter end date yyyy-mm-dd:")
                            if module_id and module_name and start_date and end_date:
                                flag_craete=create_module("create_module.json",module_id,module_name,start_date,end_date)
                                if flag_craete:
                                    print("create a module sucessfully")
                                else:
                                    print("module not sucessfully created ")
                            else:
                                print("enter a credintials sucessfully")
                        if module_choice==2:
                            filename=input("enter a filename:")
                            file_data=module_view(filename)
                            for i in file_data:
                                for k,v in  i.items():
                                    print(k,"----->",v)
                                print()
                               # print(i)
                        
                        if module_choice==4:
                            filename=input("enter a file name:")
                            module_id=int(input("enter a module_id:"))
                            flag_delete=delete_module(filename,module_id)
                            if flag_delete:
                                print(f"module id: {module_id} is deleted sucessfully!")
                            else:
                                print(f"module id: {module_id} is  not deleted sucessfully!")
                        if module_choice==3:
                            filename=input("ente a file name:")
                            module_id=int(input("enter module id:"))
                            module_name=input("enter a module name:")
                            start_date=input("enter start date yyyy-mm-dd:")
                            end_date=input("enter end date yyyy-mm-dd:")
                            flag_update=update_module(filename,module_id,module_name,start_date,end_date)
                            if flag_update:
                                print("update sucessfully!")
                            else:
                                print("update not sucessfully!")
                        if module_choice==5:
                            exit()
                else:
                    print("login failed")

            if login_choice==2:
                email=input("enter a email: ")
                Password=input("enter a password:")
                login_flag=login("student_details.json",email,Password)
                if login_flag:
                    print("login sucessfully")
                else:
                    print("login failed")

                                               

    

                    
                







        


