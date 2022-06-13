def add_time(hora_inicial,hora_adicional,day = ""):
    WEEK_DAYS= ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    
    #usar formato 24 horas
    hora_inicial = hora_inicial.split(" ")

    hora_inicial = hora_inicial[0].split(":")


    hora_inicial.append(day)
    print(hora_inicial)


def main():
    add_time("3:00 PM", "3:10")
    add_time("4:00 PM", "3:11","monday")

if  __name__ == "__main__":
    main()
