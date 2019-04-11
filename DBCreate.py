import sqlite3

conn = sqlite3.connect("Server.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

##########################
###Main tables createng###
##########################

# Create table Users
cursor.execute("""CREATE TABLE Users
                  (Name_First TEXT, Name_Second TEXT ,  Acsess_level INTEGER, User_Name TEXT ,
                   User_Password TEXT, Last_update TEXT , Online INTEGER,PRIMARY KEY(Name_First,Name_Second,User_Name,Last_update))      
               """)
conn.commit()
#Create table Teachers from table Users
cursor.execute("""CREATE TABLE Teachers
                  (Name_First TEXT, Name_Second TEXT, User_Name TEXT , Graduation TEXT, Last_update TEXT, Crated_Test_ID INTEGER ,
                  FOREIGN KEY(Name_First) REFERENCES Users(Name_First),FOREIGN KEY(Name_Second) REFERENCES Users(Name_Second),
                  FOREIGN KEY(User_Name) REFERENCES Users(User_Name),FOREIGN KEY(Last_update) REFERENCES Users(Last_update),
                  PRIMARY KEY(User_Name,Crated_Test_ID)
                  )
               """)
conn.commit()
#Create table Students from table Users
cursor.execute("""CREATE TABLE Students
                  (Name_First TEXT , Name_Second TEXT , Student_Number TEXT , Last_update TEXT, RTest_ID INTEGER , Sudent_Group TEXT,
                  FOREIGN KEY(Name_First) REFERENCES Users(Name_First),FOREIGN KEY(Name_Second) REFERENCES Users(Name_Second),
                  FOREIGN KEY(Student_Number) REFERENCES Users(User_Name),FOREIGN KEY(Last_update) REFERENCES Users(Last_update),
                  PRIMARY KEY(Student_Number, RTest_ID,RTest_ID))
               """)
#Create table Test
cursor.execute("""CREATE TABLE Tests
                  (Test_ID integer, Test_Name text, Teacher_Name text ,Test_Date date, Users_passed integer,
                   FOREIGN KEY(Test_ID) REFERENCES Teachers(Crated_Test_ID),FOREIGN KEY(Teacher_Name) REFERENCES Teachers(User_Name),
                   PRIMARY KEY(Test_ID, Test_Name))
               """)

##########################
###Test levels Creating###
##########################

#Create table TestC_Level
cursor.execute("""CREATE TABLE TestC_Level
                  (Test_ID integer PRIMARY KEY, Question_Text text, Ans_1 text, Ans_2 text, Ans_3 text, Ans_4 text, Answer integer NOT NULL,
                   FOREIGN KEY(Test_ID) REFERENCES Tests(Test_ID))
               """)
#Create table TestB_Level
cursor.execute("""CREATE TABLE TestB_Level
                  (Test_ID integer PRIMARY KEY, Question_Text text,  Answer text,
                   FOREIGN KEY(Test_ID) REFERENCES Tests(Test_ID))
               """)
#Create table TestA_Level
cursor.execute("""CREATE TABLE TestA_Level
                  (Test_ID integer , Task text,  LevelA_ID integer,
                  FOREIGN KEY(Test_ID) REFERENCES Tests(Test_ID),PRIMARY KEY(Test_ID, LevelA_ID))
               """)
#Create table LevelA_Data
cursor.execute("""CREATE TABLE LevelA_Data
                  (Level_ID integer PRIMARY KEY, Input_Data integer,Output_Data integer,
                  FOREIGN KEY(Level_ID) REFERENCES TestA_Level(LevelA_ID))
               """)
##########################
###Result tables Creating###
##########################

#Create table Sudent_Result conected to tables Student and Test
cursor.execute("""CREATE TABLE Student_Result
                  (Test_ID integer, Student_Name text, LevelC_Result real, 
                   LevelB_Result real, LevelA_Result real,Sum_Result real,
                   PRIMARY KEY(Test_ID, Student_Name,Sum_Result),
                  FOREIGN KEY(Test_ID) REFERENCES Tests(Test_ID), FOREIGN KEY(Student_Name) REFERENCES Students(Student_Number))
               """)
#Create table Result conected to table Test by Result_ID
cursor.execute("""CREATE TABLE Result
                  (Result_ID integer NOT NULL, Student_Name text, Result real,
                  FOREIGN KEY(Result_ID) REFERENCES Test_Result(Test_ID),FOREIGN KEY(Student_Name) REFERENCES Test_Result(Student_Name),
                  FOREIGN KEY(Result) REFERENCES Test_Result(Sum_Result))
               """)
#Create table Test_Levels conected to table Test by Result_ID
conn.commit()
conn.close()