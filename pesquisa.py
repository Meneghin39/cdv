import os
os.system('cls')

def pesquisar_curso(cursos, nome_pesquisado):

    encontrados = []

    for nome_curso in cursos.keys():
        if nome_pesquisado.lower() in nome_curso.lower():
            encontrados.append(nome_curso)

    return encontrados

cursos_disponiveis = {
    "HTML": None,
    "CSS": None,
    "React": None,
    "Javascript ": None,
    "Node.js": None,
    "PHP": None,
    "MySQL": None,
    "SQL": None,
    "Azure": None,
    "AWS": None,
}

nome = input("Digite o nome ou parte do nome do curso que deseja pesquisar: ")

resultados = pesquisar_curso(cursos_disponiveis, nome)

if resultados:
    print("\nCursos encontrados:")
    for curso in resultados:
        print(f"- {curso}")
else:
    print("\nNenhum curso encontrado com esse nome.")