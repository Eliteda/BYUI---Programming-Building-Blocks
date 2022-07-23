
with open("C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\txt\\life-expectancy.csv") as data:
    
    choose_year = int(input("Enter the year of interest (between 1770 - 2019): "))

    larger = 999999
    minimun = 000000
    larger_name = ""
    minimun_name = ""
    minimun_year = 0
    larger_year = 0

    larger_choose = 9999
    minimun_choose = 0
    choose_max_name = ""
    choose_min_name = ""
    choose_year_max = 0
    choose_year_min = 0
    
    for i in data:
        
        separed = i.split(",")

        country = separed[0]
        sigla = separed[1]
        year = int(separed[2])
        idade = float(separed[3])
    
        if idade > minimun:
            minimun = idade
            minimun_name = country
            minimun_year = year
        if idade <= larger:
            larger = idade
            larger_name = country
            larger_year = year
        
        if choose_year == year:
            avg = minimun + larger / len(separed[3])
            if idade > minimun_choose:
                minimun_choose = idade
                choose_min_name = country
                choose_year_min = year
            elif idade <= larger_choose:
                larger_choose = idade
                choose_max_name = country
                choose_year_max = year
    
    
    

print(f"The overall min life expectancy is: {larger} from {larger_name} in {minimun_year}")
print(f"The overall max life expectancy is: {minimun} from {minimun_name} in {larger_year}")
print()
print(f"For the year {choose_year}:")
print(f"The average life expectancy across all countries was {avg:.2f}")
print(f"The min life expectancy was in {choose_max_name} with {larger_choose}")
print(f"The max life expectancy was in {choose_min_name} with {minimun_choose}")


