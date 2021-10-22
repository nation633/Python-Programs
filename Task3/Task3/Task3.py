#This program will add new characters to a string and also convert lower case characters to upper case

hero="super man"

#Converts lower case to upper case characters
hero=hero.upper()

#adds new characters to the string
hero= hero[:1] + "^" + hero[1:]
hero= hero[:3] + "^" + hero[3:]
hero= hero[:5] + "^" + hero[5:]
hero= hero[:7] + "^" + hero[7:]
hero= hero[:11] + "^" + hero[11:]
hero= hero[:13] + "^" + hero[13:]

print(hero)

