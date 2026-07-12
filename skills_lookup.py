import loader
import search
import display

data = loader.load_data("skills.json")

if data is not None:
    while True:
        name = input("Skill name(or quit): ")
        if name == 'quit':
            break
        result = search.find_skill(data, name)
        if result is None:
            print("Not Found")
        else:
            print(display.format_skill(name,result))

