import os

os.system('cls')


def filtrar_area():
    cursos_por_area = {
        "front-end": ["HTML", "CSS", "JavaScript", "React"],
        "back-end": ["Python", "Java", "Node.js", "PHP"],
        "mobile": ["Flutter", "Reacmct Native", "Kotlin", "Swift"],
        "banco de dados": ["Modelagem de Dados", "MySQL", "SQL", "Oracle Database"],
        "nuvem": ["AWS", "Azure", "Google Cloud", "DevOps com Cloud"]
    }

    while True:
        print("\nEscolha uma área:")
        print("1 - Front-end")
        print("2 - Back-end")
        print("3 - Mobile")
        print("4 - Banco de Dados")
        print("5 - Nuvem")
        area_digitada = input("\nÁrea escolhida: ").strip().lower()

        match area_digitada:
            case "front-end" | "frontend":
                area = "front-end"
                break
            case "back-end" | "backend":
                area = "back-end"
                break
            case "mobile":
                area = "mobile"
                break
            case "banco de dados" | "bd":
                area = "banco de dados"
                break
            case "nuvem" | "cloud":
                area = "nuvem"
                break
            case _:
                print("\nÁrea inválida! Por favor, digite uma das áreas disponíveis.")

    print("\nCursos disponíveis nessa área:")
    for curso in cursos_por_area[area]:
        print(f"- {curso}")

filtrar_area()