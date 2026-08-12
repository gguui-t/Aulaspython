arquivo = input("Digite o nome do arquivo: ")

if arquivo.endswith(".jpg") or arquivo.endswith(".png"):
    print("Arquivo aceito.")
else:
    print("Arquivo não aceito.")
    
