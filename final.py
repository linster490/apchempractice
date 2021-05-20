from math import gcd
import random
ions = [{'name':'dihydrogen phosphate','formula':'H2PO4 -'},{'name':'acetate','formula':'C2H3O2 -'},{'name':'hydrogen sulfite','formula':'HSO3 -'},{'name':'hydrogen sulfate','formula':'HSO4 -'},{'name':'hydrogen carbonate','formula':'HCO3 -'},{'name':'nitrite','formula':'NO2 -'},{'name':'nitrate','formula':'NO3 -'},{'name':'cyanide','formula':'CN -'},{'name':'hydroxide','formula':'OH -'},{'name':'permanganate','formula':'MnO4 -'},{'name':'hypochlorite','formula':'ClO -'},{'name':'chlorite','formula':'ClO2 -'},{'name':'chlorate','formula':'ClO3 -'},{'name':'perchlorate','formula':'ClO4 -'},{'name':'hydrogen phosphate','formula':'HPO4 2-'},{'name':'oxalate','formula':'C2O4 2-'},{'name':'sulfite','formula':'SO3 2-'},{'name':'sulfate','formula':'SO4 2-'},{'name':'carbonate','formula':'CO3 2-'},{'name':'chromate','formula':'CrO4 2-'},{'name':'dichromate','formula':'Cr2O7 2-'},{'name':'silicate','formula':'SiO3 2-'},{'name':'phosphite','formula':'PO3 3-'},{'name':'phosphate','formula':'PO4 3-'},{'name':'ammonium','formula':'NH4 +'},{'name':'arsenate','formula':'AsO4 3-'},{'name':'peroxide','formula':'O2 2-'},{'name':'borate','formula':'BO3 3-'},{'name':'thiosulfate','formula':'S2O3 2-'},{'name':'formate','formula':'CHO2 -'},{'name':'hydronium','formula':'H3O +'},{'name':'hydrogen','formula':'H +'},{'name':'lithium','formula':'Li +'},{'name':'sodium','formula':'Na +'},{'name':'potassium','formula':'K +'},{'name':'rubidium','formula':'Rb +'},{'name':'cesium','formula':'Cs +'},{'name':'silver','formula':'Ag +'},{'name':'magnesium','formula':'Mg 2+'},{'name':'calcium','formula':'Ca 2+'},{'name':'strontium','formula':'Sr 2+'},{'name':'barium','formula':'Ba 2+'},{'name':'zinc','formula':'Zn 2+'},{'name':'cadmium','formula':'Cd 2+'},{'name':'aluminum','formula':'Al 3+'},{'name':'bismuth','formula':'Bi 3+'},{'name':'hydride','formula':'H -'},{'name':'fluoride','formula':'F -'},{'name':'chloride','formula':'Cl -'},{'name':'bromide','formula':'Br -'},{'name':'iodide','formula':'I -'},{'name':'oxide','formula':'O 2-'},{'name':'sulfide','formula':'S 2-'},{'name':'nitride','formula':'N 3-'},{'name':'phosphide','formula':'P 3-'},{'name':'carbide','formula':'C 4-'}]
list_of_cations =[{'name':'Aluminum','formula':'Al 3+'},{'name':'Ammonium','formula':'NH4 +'},{'name':'Barium','formula':'Ba 2+'},{'name':'Calcium','formula':'Ca 2+'},{'name':'Chromium(II)','formula':'Cr 2+'},{'name':'Chromium(III)','formula':'Cr 3+'},{'name':'Copper(I)','formula':'Cu +'},{'name':'Copper(II)','formula':'Cu 2+'},{'name':'Iron(II)','formula':'Fe 2+'},{'name':'Iron(III)','formula':'Fe 3+'},{'name':'Lithium','formula':'Li +'},{'name':'Magnesium','formula':'Mg 2+'},{'name':'Mercury(I)','formula':'Hg2 2+'},{'name':'Mercury(II)','formula':'Hg 2+'},{'name':'Potassium','formula':'K +'},{'name':'Silver','formula':'Ag +'},{'name':'Sodium','formula':'Na +'},{'name':'Strontium','formula':'Sr 2+'}]
list_of_anions = [{'name':'Hydride','formula':'H -'},{'name':'Floride','formula':'F -'},{'name':'Chloride','formula':'Cl -'},{'name':'Bromide','formula':'Br -'},{'name':'dihydrogen phosphate','formula':'H2PO4 -'},{'name':'acetate','formula':'C2H3O2 -'},{'name':'hydrogen sulfite','formula':'HSO3 -'},{'name':'hydrogen sulfate','formula':'HSO4 -'},{'name':'hydrogen carbonate','formula':'HCO3 -'},{'name':'nitrite','formula':'NO2 -'},{'name':'nitrate','formula':'NO3 -'},{'name':'cyanide','formula':'CN -'},{'name':'hydroxide','formula':'OH -'},{'name':'permanganate','formula':'MnO4 -'},{'name':'hypochlorite','formula':'ClO -'},{'name':'chlorite','formula':'ClO2 -'},{'name':'chlorate','formula':'ClO3 -'},{'name':'perchlorate','formula':'ClO4 -'},{'name':'hydrogen phosphate','formula':'HPO4 2-'},{'name':'oxalate','formula':'C2O4 2-'},{'name':'sulfite','formula':'SO3 2-'},{'name':'sulfate','formula':'SO4 2-'},{'name':'carbonate','formula':'CO3 2-'},{'name':'chromate','formula':'CrO4 2-'},{'name':'dichromate','formula':'Cr2O7 2-'},{'name':'silicate','formula':'SiO3 2-'},{'name':'phosphite','formula':'PO3 3-'},{'name':'phosphate','formula':'PO4 3-'},{'name':'arsenate','formula':'AsO4 3-'},{'name':'peroxide','formula':'O2 2-'},{'name':'borate','formula':'BO3 3-'},{'name':'thiosulfate','formula':'S2O3 2-'},{'name':'formate','formula':'CHO2 -'}]
acids_and_bases = [{"formula":"HCl","type":"acid","strength":"strong"},{"formula":"HBr","type":"acid","strength":"strong"},{"formula":"HI","type":"acid","strength":"strong"},{"formula":"HClO3","type":"acid","strength":"strong"},{"formula":"HClO4","type":"acid","strength":"strong"},{"formula":"HNO3","type":"acid","strength":"strong"},{"formula":"H2SO4","type":"acid","strength":"strong"},{"formula":"NaOH","type":"base","strength":"strong"},{"formula":"H2SO4","type":"acid","strength":"weak"},{"formula":"HNO2","type":"acid","strength":"weak"},{"formula":"H3PO4","type":"acid","strength":"weak"},{"formula":"NH3","type":"base","strength":"weak"}]
while True:
    mode = input("press 1 to test common ion formulas, 2 to test common ion compound formulas, 3 to test acid/bases, 4 to test solubility rules")
    if mode == "1":
        while True:
            random_ion = random.choice(ions)
            answer = input(f'what is the formula for {random_ion["name"]}')
            print('correct' if answer == random_ion["formula"] else f'wrong, correct answer was {random_ion["formula"]}')

    elif mode == "2":
        while True:
            cation = random.choice(list_of_cations)
            anion = random.choice(list_of_anions)
            cat_charge = 1 if cation["formula"][len(cation["formula"])-2]==' ' else int(cation["formula"][len(cation["formula"])-2])
            an_charge = 1 if anion["formula"][len(anion["formula"])-2]==' ' else int(anion["formula"][len(anion["formula"])-2])
            greatest_common_denom = gcd(cat_charge,an_charge)
            if greatest_common_denom != 1:
                cat_charge = cat_charge//greatest_common_denom
                an_charge = an_charge//greatest_common_denom
            answer = cation["formula"].split()[0]+str(an_charge)+"("+anion["formula"].split()[0]+")"+str(cat_charge)
            answer = answer.replace("1","")
            user_answer = input(f'what is the formula for {cation["name"]} {anion["name"]}')
            print('correct' if user_answer==answer else f'wrong, correct answer was {answer}')


    elif mode == "3":
        while True:
            random_acid_base = random.choice(acids_and_bases)
            answer = input(f'classify {random_acid_base["formula"]}, ex: weak acid')
            if random_acid_base["strength"] + ' ' + random_acid_base["type"] == answer:
                print("correct")
            else:
                print("incorrect, correct answer was " + str(random_acid_base["strength"] + ' ' + random_acid_base["type"]))
    else:
        while True:

            cation = random.choice(list_of_cations)
            anion = random.choice(list_of_anions)
            cat_charge = 1 if cation["formula"][len(cation["formula"]) - 2] == ' ' else int(
                cation["formula"][len(cation["formula"]) - 2])
            an_charge = 1 if anion["formula"][len(anion["formula"]) - 2] == ' ' else int(
                anion["formula"][len(anion["formula"]) - 2])
            greatest_common_denom = gcd(cat_charge, an_charge)
            if greatest_common_denom != 1:
                cat_charge = cat_charge // greatest_common_denom
                an_charge = an_charge // greatest_common_denom
            answer = cation["formula"].split()[0] + str(an_charge) + "(" + anion["formula"].split()[0] + ")" + str(
                cat_charge)
            compound_formula = answer.replace("1", "")
            solubility = False
            if cation["formula"].split()[0] in ["Li","Rb","Na","K","Cs","NO3","NO2","C2H3O2","HCO3","ClO3","ClO4"]:
                solubility = True
            elif (anion["formula"].split()[0] in ["Cl","Br","I"]) and (cation["formula"].split()[0] not in ["Ag","Pb","Hg2"]):
                solubility = True
            elif (anion["formula"].split()[0] == "SO4") and (cation["formula"].split()[0] not in ["Ag","Pb","Ca","Sr","Ba"]):
                solubility = True
            elif (anion["formula"].split()[0] == "OH") and (cation["formula"].split()[0] in ["Ca","Sr","Ba"]):
                solubility = True
            elif anion["formula"].split()[0] not in ["CO3","Cr2O4","PO4","S","F"]:
                continue
            ans = input(f"is {compound_formula} soluble?")
            if (solubility and ans == "yes")or (not solubility and ans == "no"):
                print("correct")
            else:
                print("incorrect")