import sys

#bs4&selenium import
#https://www.instagram.com/accounts/login/?source=auth_switcher 

#target Link for Login

#Click <div class="JRHhD">1</div>
#--> it also contains the amount of ppl who want to subscribe

def login(u,p):
    #TODO Login 
    return False



def main():
    #TODO Main Function

    username = input("Username: ")
    #could use getpass for psw (not showing the psw in the terminal)
    password =input("Passwort: ")
    
    #Authentication Error
    if not login(username,password) :
        print("failed")
        sys.exit()
    print("suceess")


def navigate():
    #Navigate to Notification Site
    pass


def refresh(url):
    #Refresh Insta Notif Site every n minutes
    pass



if __name__ == '__main__':
    main()

#TODO Error Handling
   # --> Network Errors
   # --> Login Fails
   # --> TimeOuts etc..