arquivo = open('teste.txt')
linhas = arquivo.readlines()


for i in linhas:
	
    i = i.rstrip('\n')
    print(i)
    

arquivo.close()
