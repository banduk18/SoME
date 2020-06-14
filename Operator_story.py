#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd#Подключяем модуль Пандас для работы с массивами ввиде таблицы


# In[2]:


frame = pd.read_csv('incedents.tsv', header = 0, sep = '\t')#cчитывание с файла


# In[3]:


def create_new_incedent():
    global frame
    ind = 0
    while(ind == 0):#начало ввода
        id = frame.id.iloc[-1]+1 #id
        while (ind == 0): #date
            date = []
            while(ind == 0):#year
                year=int(input("year: "))
                if (year < 0):
                    print('not correct, please try again\n')
                else:
                    ind = 1
                    date.append(year)
            ind = 0
            while(ind==0):#month
                month=int(input("month: "))
                if (month < 0 or month > 12):
                    print('not correct, please try again\n')
                else:
                    date.append(month)
                    ind = 1
            ind = 0
            while(ind==0):#day
                day=int(input("day: "))
                if (day < 0 or day > 31):
                    print('not correct, please try again\n')
                else:
                    date.append(day)
                    ind = 1
                    
        ind = 0
        while(ind==0):#type
            type_incedent = input('type of incedent (пожар, наводнение, техногенный, другие): ')
            if(type_incedent == 'пожар' or type_incedent == 'наводнение' or type_incedent == 'техногенный' or type_incedent =='другие'):
                ind = 1
            else:
                print('not correct, please, try again\n')
        ind = 0
        while(ind==0):#victims
            victims=int(input("numb of victims: "))
            if (victims < 0):
                print('not correct, please try again\n')
            else:
                ind = 1
        ind = 0
        while (ind == 0):#reinforce
            reinforce = int(input("input numb of reinforce: "))
            if (reinforce < 0):
                print('not correct, please try again\n')
            else:
                ind = 1
        ind = 0
        while (ind == 0):#adress
            adress = input("Adress: ")
            if (adress == ''):
                print('not correct, please try again\n')
            else:
                ind = 1
    new_line = {'id':id, 'date':date,'type_incedent':type_incedent,'Numb_of_victims':victims, 'Numb_of_reinforcements':reinforce, 'adress':adress}
    frame = frame.append(new_line, ignore_index = True)
        


# In[4]:


def get_incedent(id):#обращение к инциденту за id
    global frame
    return frame.iloc[id-1]


# In[5]:


def del_incedent(id):#удаление инцидента за id
    global frame
    frame = frame.drop([id-1],axis=0)


# In[6]:


def edit_incedent(id):#редактирование строки
    global frame
    ind = 0
    while(ind==0):
        editoring = input('Enter which column you want to edit: date, type_incedent, Numb_of_victims, Numb_of_reinforce, adress? ')
        if (editoring == 'date'):
            print ("Now value is: ",frame.loc[id-1,'date'])
            while (ind == 0): #date
                date = []
                while(ind == 0):#year
                    year=int(input("year: "))
                    if (year < 0):
                        print('not correct, please try again\n')
                    else:
                        ind = 1
                        date.append(year)
                ind = 0
                while(ind==0):#month
                    month=int(input("month: "))
                    if (month < 0 or month > 12):
                        print('not correct, please try again\n')
                    else:
                        date.append(month)
                        ind = 1
                ind = 0
                while(ind==0):#day
                    day=int(input("day: "))
                    if (day < 0 or day > 31):
                        print('not correct, please try again\n')
                    else:
                        date.append(day)
                        ind = 1
            frame.loc[id-1,'date']=date
        elif (editoring == 'type_incedent'):
            print ("Now value is: ",frame.loc[id-1,'type_incedent'])
            while(ind==0):#type
                type_incedent = input('type of incedent (пожар, наводнение, техногенный, другие): ')
                if(type_incedent == 'пожар' or type_incedent == 'наводнение' or type_incedent == 'техногенный' or type_incdedent =='другие'):
                    ind = 1
                else:
                    print('not correct, please, try again\n')
            frame.loc[id-1,'type_incedent']=type_incedent
        elif (editoring == 'Numb_of_victims'):
            print ("Now value is: ",frame.loc[id-1,'Numb_of_victim'])
            while(ind==0):#victims
                victims=int(input("numb of victims: "))
                if (victims < 0):
                    print('not correct, please try again\n')
                else:
                    ind = 1
            frame.loc[id-1,'Numb_of_victims']=victims
        elif (editoring == 'Numb_of_reinforce'):
            print ("Now value is: ",frame.loc[id-1,'Numb_of_reinforce'])
            while (ind == 0):#reinforce
                reinforce = int(input("input numb of reinforce: "))
                if (reinforce < 0):
                    print('not correct, please try again\n')
                else:
                    ind = 1
            frame.loc[id-1,'Numb_of_reinforce']=reinforce
        elif(editoring == 'adress'): 
            print ("Now value is: ",frame.loc[id-1,'adress'])
            while (ind == 0):#adress
                adress = input("Adress: ")
                if (adress == ''):
                    print('not correct, please try again\n')
                else:
                    ind = 1
            frame.loc[id-1,'adress']=adress
        else:
            print('Someone wrong, try again\n')
        temp = input('Do you want to change anything else in this line? y/n: ')
        if(temp=='y'):
            ind=0

