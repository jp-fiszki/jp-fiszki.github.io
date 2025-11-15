f_input = open("kanji.txt", "r", encoding="utf-8")
f_output = open("kanji.json", "w", encoding="utf-8")

f_output.write("{")
numer = 1


for linia in f_input:
    slowa = []
    slowa.append(linia.split())
    f_output.write('"'+str(numer)+'": {\n"1": "'+slowa[0][0]+'",\n"2": "'+slowa[0][1]+'",\n"3": "'+slowa[0][2]+'"\n},\n')
    numer += 1

f_output.write("}")

f_input.close()
f_output.close()