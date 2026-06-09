# my_dictionary={
#     "apple":123,
#     "orange":567,
#     "student":"id",
#     "roll_no":5
# }
# user=input("enter variable name : ")
# print(my_dictionary.get(user,"word not found"))
# output:enter variable name : appla
# word not found
# enter variable name : orange
# 567
english_nepali_dict = {
    "Apple": "स्याउ",
    "Book": "पुस्तक",
    "Cat": "बिरालो",
    "Dog": "कुकुर",
    "House": "घर",
    "School": "विद्यालय",
    "Teacher": "शिक्षक",
    "Student": "विद्यार्थी",
    "Water": "पानी",
    "Food": "खाना",
    "Sun": "घाम",
    "Moon": "चन्द्रमा",
    "Star": "तारा",
    "Tree": "रुख",
    "Flower": "फूल",
    "Road": "बाटो",
    "Car": "गाडी",
    "Bus": "बस",
    "Chair": "कुर्सी",
    "Table": "टेबल"
}
user=input("ENTERE a value for meaning : ").title()
print(english_nepali_dict.get(user,"word not found"))

