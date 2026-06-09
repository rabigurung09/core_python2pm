student={
    "cource":"bca",
    "roll_no1":{
        "name":"rabi",
        "skill":"python",
        "age":20
        
    },
    "roll_no2":{
        "name_1":"ram",
        "skill":"python with django",
        "height":5.4
        
    }
    
    
}
print(student.get("roll_no1").get("name"))
student.get("roll_no1").update({"name":"shyam"})
print(student)
INFO={
    "course":"bca",
    "roll_no1":{
        "name":"ram",
        "age":20,
        "marks":[10,20,30,40]
        
    },
    "roll_no2":{
         "name":"shyam",
        "age":35,
        "marks":[10,20,40,50]
        
    }
}

print(INFO.get("roll_no2").get("marks"))
INFO.get("roll_no2").get("marks")[3]=30

print(INFO)
print(INFO.get("roll_no2").get("marks"))
instagram={
    "name":"rabi",
    "folling":{
        "follwer":280,
        "follwing":110
    },
    "reals":{
        "folling_reals":[1,2,23,3,4,45,5]
    }
}
print(instagram.get("folling").get("follwer"))
instagram.get("reals").get("folling_reals").sort()
print(instagram)
instagram.get("reals").get("folling_reals")[5]=6
print(instagram)
instagram.get("reals").get("folling_reals")[6]=7
print(instagram)
print(instagram.get("reals").get("folling_reals"))
instagram={
    "name":"rabi",
    "folling":{
        "follwer":280,
        "follwing":110
    },
    "reals":{
        "folling_reals":[1,2,23,3,4,45,5]
    }
}
text=instagram.setdefault("ram")
print(text)