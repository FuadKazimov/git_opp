# Məqsəd: Sinifin (class) necə yaradılacağı, nümunələrin 
# (instances) necə istifadə ediləcəyi və atributlara necə müraciət 
# ediləcəyi barədə baza anlayışlarını öyrənmək.
# Təlimatlar:
#     Person adlı sinif yaradın.
#     Bu sinifdə name və age atributları olsun.
#     __init__ metodu yazaraq bu atributları təyin edin.
#     Müxtəlif name və age dəyərləri ilə iki-üç Person obyekti yaradın.
#     Hər obyektin atributlarını ekranda (print vasitəsilə) göstərin.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Fuad", 18)
person2 = Person("Ferhad", 19)
person3 = Person("Emil", 24)

print(f"Ad: {person1.name}, Yas: {person1.age}")
print(f"Ad: {person2.name}, Yas: {person2.age}")
print(f"Ad: {person3.name}, Yas: {person3.age}")

