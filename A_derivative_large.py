import os

plus_name = input("Filename with +F: ")
minus_name = input("Filename with -F: ")
field = input("Field value: ")
field = float(field)
output = input("Output name: ")

n = os.popen("grep 'Number of atoms' " + plus_name).read()
n = n[-3] + n[-2]

atom_names = os.popen("grep 'Nucleus  ' " + plus_name + "| tail -" + n).read()

plus_grep = os.popen("grep 'A(iso)' " + plus_name + "| tail -" + n).read()
minus_grep = os.popen("grep 'A(iso)' " + minus_name + "| tail -" + n).read()

plus_grep = plus_grep.split("\n")
minus_grep = minus_grep.split("\n")
atom_names = atom_names.split("\n")

for i in range(0, int(n)):
   plus_aiso = plus_grep[i]
   plus_aiso = plus_aiso.split(" ")
   plus_aiso = float(plus_aiso[-1])
   minus_aiso = minus_grep[i]
   minus_aiso = minus_aiso.split(" ")
   minus_aiso = float(minus_aiso[-1])
   atom_name = atom_names[i]
   atom_name = atom_name.split(" ")
   pointer = atom_name.index("A:ISTP=")
   atom_name = atom_name[pointer-2]

   result = ((plus_aiso - minus_aiso) * (1 / 2.8024857)) / (5.14220675 * field * 2) #result in G*m/V * 10^11
   print(atom_name + ": " + str(result))
   f = open(output, "a")
   f.write(atom_name + ": " + str(result) + "\n")
   f.close()
   print("Results saved in: ", output)
