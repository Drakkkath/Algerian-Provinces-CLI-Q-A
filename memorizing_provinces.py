import random

provinces = [
  "Adrar", "Chlef", "Laghouat", "Oum el-Bouaghi", "Batna", "Bejaia", "Biskra", "Bechar",
  "Blida", "Bouira", "Tamanghasset", "Tebessa", "Tlemcen", "Tiaret", "Tizi Ouzou","Algiers",
  "Djelfa", "Jijel", "Setif", "Saida", "Skikda", "Sidi Bel Abbes", "Annaba", "Guelma",
  "Constantine", "Medea", "Mostaganem", "M'sila", "Mascara", "Ourgla", "Oran", "El Bayadh",
  "Illizi", "Bordj Bou Arreridj", "Boumerdas", "El Taref", "Tindouf", "Tissemsilt","El Oued", "Khenchela",
  "Souk Ahras", "Tipaza", "Mila", "Ain Defla", "Naama", "Ain Temouchent", "Ghardaia", "Relizane", "El M'ghair",
  "El Menia", "Ouled Djellal", "Bordj Baji Mokhtar", "Béni Abbès", "Timimoun", "Touggourt",
  "Djanet", "In Salah", "In Guezzam"
]

#Giving user_answer a random value except 0
user_answer = 3
while user_answer!= 0:
  province = random.choice(provinces)
  print(province)
  correct_answer = provinces.index(province)+1
  user_answer = int(input())

  if user_answer == correct_answer:
    print("\tCorrect!\n")
    print("Press 0 to exit the program\n")
  elif user_answer!=0:
    print("\tIncorrect! It is ",correct_answer,"\n")
  
