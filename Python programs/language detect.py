
# Python program to demonstrate
# langdetect


from langdetect import detect


# Specifying the language for
# detection
print(detect("మూడు నాలుగేళ్లకు సరిపోయే ప్రాజెక్టులు సెట్ చేసుకున్నాడు "))
print(detect("ball"))
print(detect("Geeksforgeeks es un portal informático para geeks"))
print(detect("செம்மரக் கடத்தல் கும்பல் தலைவரான"))
print(detect("Geeksforgeeks geeks మూడు నాలుగేళ్లకు సరిపోయే ప్రాజెక్టులు సెట్ చేసుకున్నాడు "))
print(detect("Geeksforgeeksは、ギーク向けのコンピューターサイエンスポータルです。"))
