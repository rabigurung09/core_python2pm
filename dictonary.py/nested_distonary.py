student={
    "course":"bscit",
    "roll_no1":{
        "name_1":"ram",
        "age":21
    },
      "roll_no2":{
        "name":"shyam",
        "age":30
    }
}
print(student.get("roll_no1").get("name"))
student.get("roll_no1").update({"name_1":"rabi"})
print(student)
student = {
    "name": "Saroj",                 
    "age": 22,                       
    "gpa": 3.85,                     
    "is_active": True,               
    "subjects": ("Python", "Django"),
    "(1,2,3,4)" : 95,


    "details" : {
    "name":"Saroj",
    "age":26,
    "address":"Mahendranagar,Nepal",
    "weight":68.5,
    "subjects":("English","Math","Science","Biology"),
    "marks":[90,40,50,80,90,100],
    "favPlayers":["Messi","Ronaldo","Neymar"]       

}
}
student.get("details").get("marks")[3]=120
print(student)
print(student.get("details").get("marks"))
#[90, 40, 50, 120, 90, 100] 
