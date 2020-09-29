import random

provinces = [
  "Adrar", "Chlef", "Laghouat", "Oum el-Bouaghi", "Batna", "Bejaia", "Biskra", "Bechar",
  "Blida", "Bouira", "Tamanghasset", "Tebessa", "Tlemcen", "Tiaret", "Tizi Ouzou","Algiers",
  "Djelfa", "Jijel", "Setif", "Saida", "Skikda", "Sidi Bel Abbes", "Annaba", "Guelma",
  "Constantine", "Medea", "Mostaganem", "M'sila", "Mascara", "Ourgla", "Oran", "El Bayadh",
  "Illizi", "Bordj Bou Arreridj", "Boumerdas", "El Taref", "Tindouf", "Tissemsilt","El Oued", "Khenchela",
  "Souk Ahras", "Tipaza", "Mila", "Ain Defla", "Naama", "Ain Temouchent", "Ghardaia", "Relizane"
]
#answer's inital value could be anything but 0
answer = 3
while int(answer)!= 0:
  #x being the given province
  x = random.choice(provinces)
  print(x)
  correct = provinces.index(x)+1
  answer = int(input())
  if answer == correct:
    print("    Correct!\n")
  elif answer!=0:
    print("    Incorrect! It is ",correct,"\n")
