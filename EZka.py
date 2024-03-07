story = {
    "start": {
        "text":"Ви прокидаєтеся в себе в ліжку, 12 година, як ви почнете свій день.",
        "transitions": {"ПІТИ ГРАТИ В РОБЛОКС": "roblox", "ПІТИ ГРАТИ В ДОТУ": "dota"}
    },
    "roblox": {
        "text": "Ви насолодилися грою в Roblox і хочете їсти, чим перекусите?",
        "transitions": {"ПООБІДАТИ ЛОСОСЕМ": "fish", "ПООБІДАТИ ЯБЛУЧНИМ ПИРОГОМ": "tasty"}
    },
    "fish": {
        "text": "Ви отравилися лососем, він опинився не свіжим і ви в лікарні, хто вас лікуватиме?",
        "transitions": {"МЕДСЕСТРА": "medsister", "ВАШ ДАВНІЙ ЗНАЙОМИЙ": "Friend"}
    },
    "medsister": {
        "text": "Вас вилікували і ви вирішили купити їжу додому, куди ви підете за продуктами?",
        "transitions": {"ПІТИ В АТБ": "atb_food", "ПІТИ НА БАЗАР":"bad_food"}
    },
    "atb_food": {
        "text": "Ви поїли їжу з ATB i вирішили пограти в ігру, яку гру ви оберете?",
        "transitions": {"MINECRAFT": "minecraft", "CUP HEAD": "Cup_head"}
    },
    "minecraft": {
        "text": "Ви задротили Minecraft до 3 ночі, потім лягли спати і успішно прожили цей день",
        "transitions": {}
    },
    "dota": {
        "text": "Ви пограли в Dota 2 п'ять хвилин і вмерли від нервового зриву",
        "transitions": {}
    },        
    "tasty": {
        "text":  "Ви наїлися, що будете робити?",
        "transitions": {"ПІТИ В СПОРТЗАЛ": "gym", "ЛЯГТИ СПАТИ": "sleep"}
    },
    "sleep": {
        "text":  "Ви спали цілий день і ніч, ви прожили цей день і виграли",
        "transitions": {}
    },
    "gym": {
        "text": "Ви прийшли в спортзал, підняли штангу, вона виявилася надто важка і вас придавило, ви програли",
        "transitions": {}
    },
        
    "Friend": {
        "text": "Ви забули про свій борг, а знайомий ні, він ван вбив, ви програли",
        "transitions": {}
    },
    "bad_food": {
        "text": "Ви купили їжу на базарі і прийшли додому, що будете робити?",
        "transitions": {"ПОЇСТИ ЇЖУ З БАЗАРУ": "eat","НЕ ЇСТИ І ІТИ СПАТИ": "dont_eat"}
    },
    "eat": {
        "text": "їжа була зіпсована, ви вмерли і програли",
        "transitions": {}
    },
    "dont_eat": {
        "text":  "Ви поспали і прожили цей день, ви виграли",
        "transitions": {}
    },
    "Cup_head": {
        "text": "Ви пограли і на нервах пішли спати, ви виграли",
        "transitions": {},
    }
}
current_state = "start"
while True:
    state_data = story[current_state]
    print(state_data["text"])
    
    if not state_data["transitions"]:
        break
    
    options = "/".join(key for key in state_data["transitions"])
    choice = input(f"Enter your choice [{options}]: ").upper()
    
    if choice in state_data["transitions"].keys():
        current_state = state_data["transitions"][choice]
    else:
        print("Invalid choice. Try again")
               