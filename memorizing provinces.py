import random

provinces=[
  "Adrar","Chlef","Laghouat","Oum el-Bouaghi","Batna","Bejaia","Biskra","Bechar",
  "Blida","Bouira","Tamanghasset","Tebessa","Tlemcen","Tiaret","Tizi Ouzou","Algiers",
  "Djelfa","Jijel","Setif","Saida","Skikda","Sidi Bel Abbes","Annaba","Guelma",
  "Constantine","Medea","Mostaganem","M'sila","Mascara","Ourgla","Oran","El Bayadh",
  "Illizi","Bordj Bou Arreridj","Boumerdas","El Taref","Tindouf","Tissemsilt","El Oued","Khenchela",
  "Souk Ahras","Tipaza","Mila","Ain Defla","Naama","Ain Temouchent","Ghardaia","Relizane"
]
answer=3
while int(answer)!=0:
  correct=random.randrange(1,49,1)
  print(provinces[correct-1])
  answer=input()
  if int(answer)==correct:
    print("    Correct!\n")
  else:
    print("    Incorrect! It is ",correct,"\n")
