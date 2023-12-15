max_life = -1
min_life = 999999

max_year = -1
min_year = 9999999999
totalYear = float(0)

year_name_country = ''
life_expectancy = 0

min_life_expectancy = 99999999999999
max_life_expectancy = -1


add = 0
average = 0

year_interest = input('\nEnter the year of interest: ')

with open("life-expectancy.csv") as sheet:
    skip_row = next(sheet)
    
    # loop for read all the file in csv
    for line in sheet:
        
        line_clean = line.split()

        parts = line.split(',')

        # separeting all the strings
        country = parts[0]
        acronym = parts[1]
        year = parts[2]
        life_exp = float(parts[3]) # converting to FLOAT format

        # counting and calculate 
        average += 1
        add = add + life_exp
        
        result = add / average

        #figured out the max year and life expectancy
        if  life_exp > max_life:
                
                max_life = life_exp
                country_name = country
                Year_max = year

        #figured out the min year and life expectancy
        if life_exp < min_life:
             
             min_life = life_exp
             country_name_min = country
             Year_min = year

        #loop for figured out year , min and max life expectancy
        for i in year:
             if year == year_interest:
                    totalYear = year
                    year_name_country = country
                    life_expectancy = life_exp

              
                    if life_expectancy > max_life_expectancy:
                        max_life_expectancy = life_expectancy
                        name_max_expectancy = country
                        acro_max = acronym # showing creativity

                    if life_expectancy < min_life_expectancy:
                         min_life_expectancy = life_expectancy
                         name_min_expectancy = country
                         acro_min = acronym # showing creativity 

    # showing all the results
    print(f"The overall max life expectancy is: {max_life} from {country_name} in {Year_max}")
    print(f"The overall min life expectancy is: {min_life} from {country_name_min} in {Year_min}")

    print(f'\nFor the year {year_interest}:')
    print(f'The average life expectancy across all countries was {result:.2f}')
    print(f'The max life expectancy was {name_max_expectancy} - ({acro_max}) in with {max_life_expectancy}')
    print(f'The max life expectancy was {name_min_expectancy} - ({acro_min}) in with {min_life_expectancy}')
  
            


    

        
        
    

