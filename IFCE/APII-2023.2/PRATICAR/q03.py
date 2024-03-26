def naturalidade(s):
    match s:
        case "CE":
            return "cearense"
        case "PB":
            return "paraibano"
        case "PE":
            return "pernambuco"
        case _:
            return "outro estado"

sigla = input("Digite a sigla de algum estado: ")
print(naturalidade(sigla.upper()))