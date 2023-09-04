import json

dct = {}
tasks = []
user = ''
main_menu = '''1. Add task
2. Remove task
3. Display task
4. Exit
'''

def load_data():
    '''Get data from database.'''
    global dct
    with open('c:/Users/maria/OneDrive/Desktop/pythonlessons/to_do/data.json') as file:
        dct = json.load(file)
    
def save_data():
    '''Save data in database.'''
    global dct
    with open('c:/Users/maria/OneDrive/Desktop/pythonlessons/to_do/data.json','w') as file:
        json.dump(dct,file)

def registartion():
    '''Open new account.
    Checks that the registration was successful return true, else return false.'''

    username = input("enter username: ")
    password = input("enter password: ")
    if username not in dct:
       dct[username] = {'password' : password, 'tasks': []}
       save_data()
       return True
    else:
        print("There is this username in data.")
        return False



def login():
  '''Enter your to do account.
   Checks that the login was successful return true, else return false. '''
  
  username = input("enter username: ")
  password = input("enter password: ")
  load_data()
  if dct:
    if username in dct:
        global user
        if password == dct[username]['password']:
           tasks = dct[username]['tasks']
           user = username
           return True
        else:
            print("You enter false password")
    else:
        print(f"if you already have account you enter false username enter right username,\n\
              else if you want to register please enter 1, else enter any number.")
        check = input("enter the number:  ")
        if check == '1':
            if registartion():
                return True
            else:
                return False
        else:
            print("You do not want to register.")
            return False
  else:
      print("you are first user please register.")
      if registartion():
          return True
      else:
          return False      
      


def add_task(task):
    '''Add task to tasks.'''


    if task not in tasks:
       tasks.append(task)
       dct[user]['tasks'] = task
    else:
        print("you have this task.")


def remove_task(task):
    '''Delete task from tasks.'''

    if task in tasks:
        task.remove(task)
        dct[user]['tasks'] = task
    else:
        print("This dask you dont have.")


def show_task():
    '''Display tasks in screen.'''

    for task in tasks:
        print(task)

def run():
  '''Run to do app.'''

  print("Welcome to do")
  if login():
    while True:
        print(main_menu)
        check = input("enter the number that you want: ")
        if check == '1':
            task = input("enter task: ")
            add_task(task)
        elif check == '2':
            task = input("enter task: ")
            remove_task(task)
        elif check == '3':
            show_task()
        elif check == '4':
            save_data()
            break
        else:
            print("invalid check")
    else:
     print('you do nort have account.')


if __name__ == '__main__':
    run()



