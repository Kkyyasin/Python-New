first_name=["mehmet","muhammed","ahmed"]
second_name=[" ","mustafa","ibrahim","salih"]
surname=["ozdemir","tan","demir","avci"]
from random import choice
for i in range(0,10):
     print("Ad:{} {}\nsoyad:{}".format(choice(first_name),choice(second_name),choice(surname)))
