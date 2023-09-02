from enum import Enum
from helper import Stud_Acs, Student, clear_screen, load_data, save_data


school = []

def menu():
    global school
    while(True):
        for x in Stud_Acs:
            print (x.value, x.name)
        slc = Stud_Acs(int(input('select action: '))) #selection from user
        if slc == Stud_Acs.Add: 
            tmp = AddStd(school)
            school = tmp
        if slc == Stud_Acs.Add_Test: addTestToStd(school) 
        if slc == Stud_Acs.Print_all: PrintAll(school)
        if slc == Stud_Acs.Print_best: print(BestStd(school))
        if slc == Stud_Acs.Print_worst: print(WorstStd(school))
        if slc == Stud_Acs.Exit: 
            school = SortSchool(school)
            return

def addTestToStd(list):
    for i, std in enumerate(list):
        print(i+1, std)
    user_slc = int(input('select student: '))
    list[user_slc-1].addTest()

def AddStd(list):
    list.append(Student(input('Enter name: '), int(input('Enter age: '))))
    list[len(list)-1].addTest()
    tmp = SortSchool(list)
    return tmp

def SortSchool(list):
    newlist = []
    for x in range(len(list)):
        tmp = BestStd(list)
        list.remove(tmp)
        newlist.append(tmp)
    return newlist         

def PrintAll(list):
    for std in list:
        print(std)

def BestStd(list):
    if(list):
        tmp = list[0]
        for std in list:
            if(std.tests):
                if (std.average() > tmp.average()): tmp = std
            else: return None
        return tmp
    else: return None

def WorstStd(list):
    if(list):
        tmp = list[0]
        for std in list:
            if(std.tests):
                if (std.average() < tmp.average()): tmp = std
            else: return None
        return tmp
    else: return None


if __name__ == '__main__':
    clear_screen()
    school = load_data()
    menu()
    save_data(school)