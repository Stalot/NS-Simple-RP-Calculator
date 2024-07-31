import nationstates




api = nationstates.Nationstates("Hello, world")

print("WELCOME TO CALCULATOR!")

def main():

    nation_name = str(input("Nation: "))

    
    print("""""")

    if not nation_name == "":
        if api.nation(nation_name).exists() == True:
            data = api.nation(nation_name).get_shards("sectors", "tax", "gdp", "fullname", "region")


            print('Nation Found:', data["fullname"] + ", from", data["region"])
        
            print('')

            government_portion = data["sectors"].__getitem__("government")
            tax = data["tax"]
            economic_output = data["gdp"]

            revenue = float(government_portion) - float(tax)


            suplus = float(economic_output) * revenue / 100


            print("[b]RP CALCULATOR[/b]")
            print("")
            print(nation_name, "government is:", government_portion)
            print(nation_name, "tax is:", tax)
            print(nation_name, "economic output is:", economic_output)
            print("""
__________________________________________________________________________
[b]RESULT:[/b]
""")
            print(nation_name, "suplus is: ", int(suplus))
            print("")
            input("Press Enter to continue")
            print("""
            
""")

            main()
        
        # Caso nao tenha encontrado nenhuma naçao correspondente, (If nation not found):
        else:
            print("""ERROR: Nation not found

""")
        main()
   
   # If nation name is empty:
   
    else:
        print("""ERROR: Nation not found

""")
        main()

main()
