#Legend
#Hashtags will be used to highlight sections
"""
Triple double quotation marks will be used to explain each sections.
"""

#External Modules/Libraries
"""
random - is used to randomize diffferent aspects of the code.
time - used to add the concept of time, primary use for delays.
copy - to make a copy or retain attributes of different pokemon.
"""
import random
import time
import copy

#POKÉMON DATA
"""
This is a list for selecting every available pokemon you can use.
There are 10 Pokémons currently available in the game.
"""

available_pokemon = ["Pikachu", "Gardevoir", "Mew", "Piplup", "Pidgeot",
                     "Ninetales", "Absol", "Snorlax", "Lucario", "Charizard"]
"""
This is the dictionary of every Pokémon's attributes, with their assigned numerical values.
Theire moves are also stored here, together with their type, damage, category and PPs
PP or power points is a system that limits the use of skills or abilities. The PP is randomized
to make each game feel different and natural as the focus of this game is mainly about the battle
system of the Pokémon game
"""
pokemon_attributes = {
    "Pikachu": {"type": "Electric", "hp": 200, "attack": 50, "defense": 30, "special_attack": 40, "special_defense": 35, "speed": 90,
                "moves": {"Thunderbolt": {"type": "Electric", "damage": 40, "category": "special", "pp": random.randint(10, 15)},
                          "Quick Attack": {"type": "Normal", "damage": 20, "category": "physical", "pp": random.randint(15, 25)},
                          "Electro Ball": {"type": "Electric", "damage": 35, "category": "special", "pp": random.randint(10, 15)},
                          "Iron Tail": {"type": "Steel", "damage": 30, "category": "physical", "pp": random.randint(10, 15)}}},
    "Gardevoir": {"type": "Psychic", "hp": 200, "attack": 45, "defense": 40, "special_attack": 50, "special_defense": 45, "speed": 80,
                  "moves": {"Confusion": {"type": "Psychic", "damage": 30, "category": "special", "pp": random.randint(10, 15)},
                            "Psychic": {"type": "Psychic", "damage": 40, "category": "special", "pp": random.randint(10, 15)},
                            "Moonblast": {"type": "Fairy", "damage": 45, "category": "special", "pp": random.randint(5, 10)},
                            "Calm Mind": {"type": "Psychic", "damage": 0, "category": "status", "buff": {"attack": 10}, "pp": random.randint(10, 20)}}},
    "Mew": {"type": "Psychic", "hp": 200, "attack": 50, "defense": 50, "special_attack": 50, "special_defense": 50, "speed": 100,
            "moves": {"Psychic": {"type": "Psychic", "damage": 40, "category": "special", "pp": random.randint(10, 15)},
                      "Aura Sphere": {"type": "Fighting", "damage": 35, "category": "special", "pp": random.randint(10, 15)},
                      "Swift": {"type": "Normal", "damage": 25, "category": "special", "pp": random.randint(15, 25)},
                      "Recover": {"type": "Normal", "damage": 0, "category": "status", "heal": 50, "pp": random.randint(10, 20)}}},
    "Piplup": {"type": "Water", "hp": 200, "attack": 45, "defense": 40, "special_attack": 45, "special_defense": 40, "speed": 60,
               "moves": {"Water Gun": {"type": "Water", "damage": 35, "category": "special", "pp": random.randint(10, 15)},
                         "Peck": {"type": "Flying", "damage": 20, "category": "physical", "pp": random.randint(15, 25)},
                         "Bubble Beam": {"type": "Water", "damage": 30, "category": "special", "pp": random.randint(10, 15)},
                         "Ice Beam": {"type": "Ice", "damage": 40, "category": "special", "pp": random.randint(10, 15)}}},
    "Pidgeot": {"type": "Flying", "hp": 200, "attack": 60, "defense": 50, "special_attack": 45, "special_defense": 40, "speed": 95,
                "moves": {"Gust": {"type": "Flying", "damage": 30, "category": "special", "pp": random.randint(10, 15)},
                          "Quick Attack": {"type": "Normal", "damage": 20, "category": "physical", "pp": random.randint(15, 25)},
                          "Wing Attack": {"type": "Flying", "damage": 35, "category": "physical", "pp": random.randint(10, 15)},
                          "Agility": {"type": "Psychic", "damage": 0, "category": "status", "buff": {"attack": 0}, "pp": random.randint(10, 20)}}},
    "Ninetales": {"type": "Fire", "hp": 200, "attack": 50, "defense": 45, "special_attack": 60, "special_defense": 50, "speed": 100,
                  "moves": {"Flamethrower": {"type": "Fire", "damage": 40, "category": "special", "pp": random.randint(10, 15)},
                            "Confuse Ray": {"type": "Ghost", "damage": 0, "category": "status", "buff": {"confused": 1}, "pp": random.randint(10, 20)},
                            "Fire Spin": {"type": "Fire", "damage": 35, "category": "special", "pp": random.randint(10, 15)},
                            "Will-O-Wisp": {"type": "Fire", "damage": 0, "category": "status", "buff": {"burned": 1}, "pp": random.randint(10, 20)}}},
    "Absol": {"type": "Dark", "hp": 200, "attack": 65, "defense": 40, "special_attack": 50, "special_defense": 40, "speed": 75,
              "moves": {"Night Slash": {"type": "Dark", "damage": 35, "category": "physical", "pp": random.randint(10, 15)},
                        "Swords Dance": {"type": "Normal", "damage": 0, "category": "status", "buff": {"attack": 15}, "pp": random.randint(10, 20)},
                        "Bite": {"type": "Dark", "damage": 30, "category": "physical", "pp": random.randint(10, 15)},
                        "Slash": {"type": "Normal", "damage": 25, "category": "physical", "pp": random.randint(15, 25)}}},
    "Snorlax": {"type": "Normal", "hp": 300, "attack": 70, "defense": 65, "special_attack": 35, "special_defense": 55, "speed": 30,
                "moves": {"Body Slam": {"type": "Normal", "damage": 35, "category": "physical", "pp": random.randint(10, 15)},
                          "Rest": {"type": "Psychic", "damage": 0, "category": "status", "heal": 100, "pp": random.randint(10, 20)},
                          "Headbutt": {"type": "Normal", "damage": 30, "category": "physical", "pp": random.randint(10, 15)},
                          "Hyper Beam": {"type": "Normal", "damage": 50, "category": "physical", "pp": random.randint(5, 10)}}},
    "Lucario": {"type": "Fighting", "hp": 200, "attack": 65, "defense": 55, "special_attack": 50, "special_defense": 50, "speed": 70,
                "moves": {"Aura Sphere": {"type": "Fighting", "damage": 40, "category": "special", "pp": random.randint(10, 15)},
                          "Close Combat": {"type": "Fighting", "damage": 50, "category": "physical", "pp": random.randint(5, 10)},
                          "Dragon Pulse": {"type": "Dragon", "damage": 35, "category": "special", "pp": random.randint(10, 15)},
                          "Metal Claw": {"type": "Steel", "damage": 25, "category": "physical", "pp": random.randint(15, 25)}}},
    "Charizard": {"type": "Fire", "hp": 200, "attack": 60, "defense": 50, "special_attack": 60, "special_defense": 50, "speed": 100,
                  "moves": {"Flamethrower": {"type": "Fire", "damage": 40, "category": "special", "pp": random.randint(10, 15)},
                            "Fly": {"type": "Flying", "damage": 35, "category": "physical", "pp": random.randint(10, 15)},
                            "Dragon Claw": {"type": "Dragon", "damage": 45, "category": "physical", "pp": random.randint(5, 10)},
                            "Fire Spin": {"type": "Fire", "damage": 35, "category": "special", "pp": random.randint(10, 15)}}}
}
#Type Chart
"""
This chart contains the damage increase or decrease depending on the
type advantage of a Pokémon chosen to its opponet and vice versa.
"""
type_chart = {
    "Fire": {"Grass": 2.0, "Water": 0.5, "Ice": 2.0},
    "Water": {"Fire": 2.0, "Electric": 0.5, "Grass": 0.5},
    "Electric": {"Water": 2.0, "Ground": 0.0, "Flying": 2.0},
    "Grass": {"Water": 2.0, "Fire": 0.5, "Flying": 0.5},
    "Psychic": {"Fighting": 2.0, "Dark": 0.0},
    "Dark": {"Psychic": 2.0},
    "Ice": {"Flying": 2.0, "Fire": 0.5},
    "Flying": {"Grass": 2.0, "Electric": 0.5},
}
#Nature types
"""
There is a feature in the original Pokémon series wherein each Pokémon can have
different nature that affects their attributes. The nature type system in this game
only provides a visual effecto to give Pokémon's a sense of individuality and identity.
"""
natures = ["Adamant", "Modest", "Jolly", "Timid", "Bold", "Calm", "Hardy", "Naive",
           "Relaxed", "Impish", "Lax", "Careful", "Rash", "Quiet", "Sassy", "Gentle"]

#CONDITIONS
"""
Weather conditions is a feature in the game that gives a feel of the setting.
It is randomized every game.
"""
weather_conditions = ["Sunny", "Rainy", "Thunderstorm", "Snowy", "Sandstorm", "Foggy", "Windy", "None"]

#TERRAIN TYPES
"""
The same goes for the terrain types. A setting is a very important element in the game
as it allows for visualization given that this is a text-based game.
"""
terrains = ["Electric Terrain", "Grassy Terrain", "Psychic Terrain", "Misty Terrain", "Rocky Terrain", "None"]

#Copy Module Usage
"""
The purpose of this specific module and its role in the game is to save the datas
from the dictionary "pokemon_attributes". It allows for restoration of the Pokémons
that are used in previous games. Without this module, the user can battle again but
the attributes of the Pokémons are still affected by the previous battle.
"""
original_pokemon_attributes = copy.deepcopy(pokemon_attributes)
canteen_unlocked = False

#UTILITY FUNCTIONS
"""
This is the defined function that restores pokemon_attributes to their
original state
"""
def reset_pokemon_attributes():
    global pokemon_attributes
    pokemon_attributes = copy.deepcopy(original_pokemon_attributes)

"""
This defined functions prints texts slowly for different dramatic moments in the battle.
"""
def print_slowly(msg, delay=0.03):
    for ch in str(msg):
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def dramatic_effects(message):
    print_slowly(f"\n*** {message} ***", delay=0.08)

"""
This is the function that assigns random field effects to each battle.
"""
def display_random_field():
    weather = random.choice(weather_conditions)
    terrain = random.choice(terrains)
    if weather != "None":
        print_slowly(f"The battlefield is shrouded in {weather.lower()} conditions.")
    if terrain != "None":
        print_slowly(f"The ground is affected by {terrain.lower()}.")
    if weather == "None" and terrain == "None":
        print_slowly("The battlefield is calm and normal.")

"""
This is the function that assigns random nature types to Pokémons chosen per game
"""
def assign_random_nature(team):
    for pokemon in team:
        nature = random.choice(natures)
        pokemon_attributes[pokemon]["nature"] = nature
        print_slowly(f"{pokemon} has a {nature} nature!")

"""
This sets a limit so that the healing factor from healing
abilities does not exceed the max HP.
"""
def get_max_hp(name):
    return 300 if name == "Snorlax" else 200

"""
This sets up the minimum hp.
"""
def clamp_hp(pokemon):
    if pokemon_attributes[pokemon]["hp"] < 0:
        pokemon_attributes[pokemon]["hp"] = 0
    if pokemon_attributes[pokemon]["hp"] > get_max_hp(pokemon):
        pokemon_attributes[pokemon]["hp"] = get_max_hp(pokemon)

def stage_multiplier(stage):
    stage = max(-6, min(6, stage))
    return (2 + stage)/2 if stage >= 0 else 2/(2 - stage)
"""
This is one of the sub functions inside the damage calculator that
turns a boost or drop into a number that increases or decreases a stat in battle.
"""

#DAMAGE & MOVE
"""
This is one of the core functions of the game. It computes each damage taken by pokemons,
subtracting them in their hps or hitpoints. Without this function, the main purpose of this game
which is the PvP system will be useless.
"""
def calculate_damage(attacker, move_name, defender):
    move = pokemon_attributes[attacker]["moves"][move_name]
    attack = pokemon_attributes[attacker]["attack"]
    defn = pokemon_attributes[defender]["defense"]
    attack *= stage_multiplier(pokemon_attributes[attacker].get("attack_stage", 0))
    defn *= stage_multiplier(pokemon_attributes[defender].get("defense_stage", 0))
    if pokemon_attributes[attacker].get("status") == "Burned":
        attack *= 0.5
    defn = max(1, defn)
    base_damage = move["damage"] * (attack / defn)
    crit = False
    if random.random() < 0.10:
        base_damage *= 1.5
        crit = True
    effectiveness = type_chart.get(pokemon_attributes[attacker]["type"], {}).get(pokemon_attributes[defender]["type"], 1)
    base_damage *= effectiveness
    return max(1, int(base_damage)), crit, effectiveness

"""
It decides what happens when a Pokémon uses a move. The purpose of this
code is to check what type of move is used and apply damage accordingly.
"""
def apply_move(attacker, move_name, defender):
    move = pokemon_attributes[attacker]["moves"].get(move_name, {"damage": 20, "category": "physical", "pp": 999})
    if move.get("pp", 999) > 0:
        move["pp"] -= 1
    else:   
        print_slowly(f"{attacker} has no PP left for {move_name}! Using Struggle!")
        move_name = "Struggle"
        move = {"damage": 20, "category": "physical", "pp": 999}
    #Confusion
    if pokemon_attributes[attacker].get("status") == "Confused" and random.random() < 0.5:
        dmg = max(1, int(pokemon_attributes[attacker]["attack"] * 0.3))
        pokemon_attributes[attacker]["hp"] -= dmg
        clamp_hp(attacker)
        print_slowly(f"{attacker} is confused and hurt itself for {dmg} HP!")
        return
    dmg, crit, eff = calculate_damage(attacker, move_name, defender)
    pokemon_attributes[defender]["hp"] -= dmg
    clamp_hp(defender)
    msg = f"{attacker} used {move_name}! It dealt {dmg} damage."
    if crit:
        msg += " A critical hit!"
    if eff > 1:
        msg += " It's super effective!"
    elif eff < 1:
        msg += " It's not very effective..."
    print_slowly(msg)
    #Heal
    if "heal" in move and move["heal"] > 0:
        pokemon_attributes[attacker]["hp"] += move["heal"]
        clamp_hp(attacker)
        print_slowly(f"{attacker} heals for {move['heal']} HP!")
    #Buffs/debuffs
    if "buff" in move:
        for eff, val in move["buff"].items():
            if eff == "attack":
                pokemon_attributes[attacker]["attack"] += val
                print_slowly(f"{attacker}'s attack rises by {val}!")
            elif eff == "burned":
                pokemon_attributes[defender]["status"] = "Burned"
                print_slowly(f"{defender} is burned!")
            elif eff == "confused":
                pokemon_attributes[defender]["status"] = "Confused"
                print_slowly(f"{defender} became confused!")

#DISPLAY
"""
This section contains all the code for how information
is displayed to the player. This includes the following:
  *Pokemon Hitpoints
  *Pokemon Fullstats
  *Pokemon moves
  *Pokemon taking damage
Anthing that is displayed during the battle process comes from here.
"""
def display_pokemon_hp(name):
    print_slowly(f"{name} | HP: {pokemon_attributes[name]['hp']}/{get_max_hp(name)}")

def display_pokemon_status(name):
    p = pokemon_attributes[name]
    print(f"\n{name}'s Status:")
    print(f"Type: {p['type']}")
    print(f"HP: {p['hp']}/{get_max_hp(name)}")
    print(f"Attack: {p['attack']}")
    print(f"Defense: {p['defense']}")
    print(f"Special Attack: {p['special_attack']}")
    print(f"Special Defense: {p['special_defense']}")
    print(f"Speed: {p['speed']}")
    print(f"Nature: {p.get('nature', 'None')}")
    print(f"Status: {p.get('status', 'None')}")
    print("Moves:")
    for move, stats in p["moves"].items():
        dmg = stats.get("damage", 0)
        heal = stats.get("heal", 0)
        pp = stats.get("pp", 0)
        effect = ""
        if "buff" in stats:
            effect = ", ".join(f"{k}: {v}" for k,v in stats["buff"].items())
        info = f"  {move} | DMG: {dmg} | Heal: {heal} | PP: {pp}"
        if effect:
            info += f" | Effect: {effect}"
        print(info)

def choose_move(name):
    moves = pokemon_attributes[name]["moves"]
    while True:
        available_moves = [m for m in moves if moves[m]["pp"] > 0]
        if not available_moves:
            print_slowly(f"{name} has no PP left! Using Struggle!")
            return "Struggle"
        print("\n=== Move Selection ===")
        for i, m in enumerate(moves, 1):
            move = moves[m]
            dmg_text = f"DMG: {move['damage']}" if move.get("damage",0)>0 else ""
            heal_text = f"Heal: {move['heal']}" if move.get("heal",0)>0 else ""
            effect_text = ""
            if "buff" in move:
                effects = []
                for eff,val in move["buff"].items():
                    if eff=="attack": effects.append(f"+ATK {val}")
                    elif eff=="burned": effects.append("Burn")
                    elif eff=="confused": effects.append("Confuse")
                    else: effects.append(eff.capitalize())
                if effects: effect_text=" | Effect: "+", ".join(effects)
            info_parts = [txt for txt in (dmg_text, heal_text) if txt]
            info_string = " | ".join(info_parts) if info_parts else "No Direct Effect"
            status = "" if m in available_moves else "(No PP)"
            print(f"{i}. {m:<15} | {info_string} | PP: {move['pp']}{effect_text} {status}")
        choice_input = input("\nChoose move (number or name): ").strip()
        if choice_input.isdigit():
            idx=int(choice_input)-1
            if 0<=idx<len(moves):
                selected=list(moves.keys())[idx]
                if moves[selected]["pp"]>0: return selected
                else: print("That move has no PP left. Choose another move.")
        else:
            for m in moves:
                if choice_input.lower()==m.lower() and moves[m] ["pp"]>0:
                    return m
            print("Invalid move. Try again.")

#BATTLE LOOP
"""
This serves as the main battle engine of the entire game. This part does the following:
1. Saves original Pokémon stats
2. Sets the pokemon teams
3. Randomly assigns natures
4. Repeats this until the fight is over
    Lets the player view status
    Lets the player switch pokemon
    Gets player move → applies it
    Apply pp system
    Gets opponent move → applies it
    Checks for fainted pokemon
    Brings out new pokemon automatically
5. Announces winner
6. Restores original stat
"""
def battle_loop(player_name, player_team, opponent_name, opponent_team, mode_choice=2):
    assign_random_nature(player_team)
    assign_random_nature(opponent_team)
    display_random_field()

    player_active = player_team[0]
    opponent_active = opponent_team[0]

    while player_team and opponent_team:
        #Display current HPs
        print("\n--- Battle Status ---")
        display_pokemon_hp(player_active)
        display_pokemon_hp(opponent_active)

        #Player Options
        while True:
            print("\nOptions:")
            print("1. Fight")
            if len(player_team) > 1:
                print("2. Switch Pokémon")
            print("3. View Team Status")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                move = choose_move(player_active)
                apply_move(player_active, move, opponent_active)
                break

            elif choice == "2" and len(player_team) > 1:
                print("\nYour available Pokémon:")
                for i, p in enumerate(player_team):
                    print(f"{i+1}. {p} (HP: {pokemon_attributes[p]['hp']}/{get_max_hp(p)})")
                while True:
                    try:
                        idx = int(input("Choose Pokémon to switch: ")) - 1
                        if 0 <= idx < len(player_team) and player_team[idx] != player_active:
                            player_active = player_team[idx]
                            dramatic_effects(f"{player_active} enters the battlefield!")
                            break
                    except:
                        pass
                    print("Invalid choice, try again.")
                break

            elif choice == "3":
                print_slowly(f"\n{player_name}'s Team Status:")
                for p in player_team:
                    display_pokemon_status(p)

            else:
                print("Invalid option. Try again.")

        #Check if opponent fainted
        if pokemon_attributes[opponent_active]["hp"] <= 0:
            print_slowly(f"{opponent_active} fainted!")
            opponent_team.remove(opponent_active)
            if opponent_team:
                opponent_active = opponent_team[0]
                dramatic_effects(f"{opponent_active} enters the battlefield!")
            else:
                return player_name

        #Opponent Turn
        if opponent_team:
            # AI logic: switch if active Pokémon is low HP and has others
            if len(opponent_team) > 1 and pokemon_attributes[opponent_active]["hp"] < get_max_hp(opponent_active) * 0.3:
                for p in opponent_team:
                    if p != opponent_active and pokemon_attributes[p]["hp"] > 0:
                        opponent_active = p
                        dramatic_effects(f"{opponent_name} switches to {opponent_active}!")
                        break

            opp_move = random.choice([m for m in pokemon_attributes[opponent_active]["moves"] if pokemon_attributes[opponent_active]["moves"][m]["pp"] > 0] or ["Struggle"])
            apply_move(opponent_active, opp_move, player_active)

            if pokemon_attributes[player_active]["hp"] <= 0:
                print_slowly(f"{player_active} fainted!")
                player_team.remove(player_active)
                if player_team:
                    player_active = player_team[0] 
                    dramatic_effects(f"{player_active} enters the battlefield!")
                else:
                    return opponent_name

    return player_name if player_team else opponent_name

#TEAM SELECTION
"""
This part allows the trainer to pick a pokemon. Assign a random pokemon to the CPU.
Also makes sure that only existing pokemon are chosen.
"""
def choose_team(player, team_size):
    team=[]
    print_slowly(f"\n{player}, choose your team of {team_size} Pokémon!")
    available = available_pokemon
    while len(team)<team_size:
        for i,p in enumerate(available,1):
            print(f"{i}. {p}")
        choice=input("Enter Pokémon name or number: ").strip()
        if choice.isdigit():
            idx=int(choice)-1
            if 0<=idx<len(available):
                team.append(available[idx])
                available.pop(idx)
            else:
                print("Invalid number.")
        else:
            if choice in available:
                team.append(choice)
                available.remove(choice)
            else:
                print("Invalid Pokémon name.")
    print_slowly(f"{player}'s team: {team}")
    return team

def generate_cpu_team(team_size,):
    available= available_pokemon
    return random.sample(available, team_size)

#STORY MODE & CANTEEN PLACEHOLDERS
"""
Thin wrapper around battle_loop.
Returns True if the player (player_name) won, False otherwise.
"""
def run_battle(player_name, player_team, opponent_name, opponent_team, mode_choice):
    winner = battle_loop(player_name, player_team, opponent_name, opponent_team, mode_choice)
    return winner == player_name
"""
Mark the canteen as unlocked and notify the player (does not auto-enter).
"""
def unlock_canteen():
    global canteen_unlocked
    if not canteen_unlocked:
        canteen_unlocked = True
        print_slowly("\nYou unlocked the Canteen of the Heroes! Visit it from the main menu.")
    else:
        print_slowly("\nCanteen already unlocked.")
"""
This is the Story Mode, and the order of the computer opponents are fixed.
"""
def story_mode(player_name, player_team):
    print("\n==== STORY MODE BEGIN ====")
    print_slowly(f"Welcome, Trainer {player_name}! Your journey in Pytheria Online begins now.")
    input("\nPress Enter to load into the Digital Realm…")

    #Intro fight
    print_slowly("\n--- SYSTEM ALERT ---")
    print_slowly("Digital instability detected in Startup Plains.")
    enemy_team = ["Pidgeot"]
    print_slowly("\nA corrupted Pidgeot glitching through the sky dives at you!")
    run_battle(player_name, player_team.copy(), "Pidgeot", enemy_team, mode_choice=2)
    final_boss = ["Charizard", "Ninetales", "Lucario"]
    input("\nPress Enter to continue…")
    print_slowly("\n--- GLITCH FIELDS ---")

    #Final boss battle: capture whether player actually won
    player_won_final = run_battle(player_name, player_team.copy(), "Admin Overlord", final_boss, mode_choice=2)

    if player_won_final:
        # only show congrats and unlock canteen when player truly wins
        print_slowly("""\nAt Mt. Bugnut.exe, you confront the rogue data‑modder responsible for the chaos—defeating\n their overclocked boss Pokémon restores the server, earning you peace, glory, and unlimited virtual rice.""")
        print_slowly("\nThe glitches fade... Pytheria Online stabilizes.")
        print_slowly("🎉 CONGRATULATIONS! You finished Story Mode!The Canteen Password is: unlirice")
        unlock_canteen()   # grant the canteen unlock / flag
    else:
        # player lost final boss
        print_slowly("\nYou were defeated by the Admin Overlord. GL next time, Trainer — return to the main menu to try again.")
        # restore any needed state already happens in battle_loop; just return to menu
        return
"""
The defining feature of the game that can only be unlocked when the story mode is finished.
"""
def canteen_of_the_heroes():
    print("\n=== CANTEEN OF THE HEROES ===")
    print("Only true champions may enter.")
    print("Please type the password to continue:")
    user_pw = input("> ")
    correct_pw = "unlirice"
    if user_pw == correct_pw:
        print("\nAccess granted!")
        print("Welcome to the legendary Canteen of the Heroes!")
        print("You are immediately served...")
        print("🥢🍚 *A MOUNTAIN OF UNLI RICE!* 🍚🥢")
        print("The rice refills itself every time you blink.")
        print("A waiter whispers: 'Tread responsibly trainer… or the rice will consume you.'")
    else:
        print("\nAccess denied! The rice spirits only accept the strong, go back weakling!")
        print("A lone grain of rice rolls across the floor judging you…1")

#BANNER
def print_banner():
    print_slowly("\n"
          "░█▀▀█ █──█ ▀▀█▀▀ █──█ █▀▀█ █▀▀▄\n"
          "░█▄▄█ █▄▄█ ──█── █▀▀█ █──█ █──█\n"
          "░█─── ▄▄▄█ ──▀── ▀──▀ ▀▀▀▀ ▀──▀")
    print_slowly("\n"
          "░█▀▀█ █▀▀█ █─█ █▀▀ █▀▄▀█ █▀▀█ █▀▀▄\n"
          "░█▄▄█ █──█ █▀▄ █▀▀ █─▀─█ █──█ █──█\n"
          "░█─── ▀▀▀▀ ▀─▀ ▀▀▀ ▀───▀ ▀▀▀▀ ▀──▀")
    print_slowly("\n"
          "░█▀▀▀█ █──█ █▀▀█ █───█ █▀▀▄ █▀▀█ █───█ █▀▀▄\n"
          "─▀▀▀▄▄ █▀▀█ █──█ █▄█▄█ █──█ █──█ █▄█▄█ █──█\n"
          "░█▄▄▄█ ▀──▀ ▀▀▀▀ ─▀─▀─ ▀▀▀─ ▀▀▀▀ ─▀─▀─ ▀──▀")

#MAIN MENU
"""
This is the compilation of all the functions created and used to create the python-based and text-driven
Pokémon game.
"""
def start_game():
    reset_pokemon_attributes()
    print_banner()
    global canteen_unlocked
    while True:
        print("\nMain Menu")
        print("1. Start Free Battle")
        print("2. Rules")
        print("3. Game Mechanics")
        print("4. Backstory")
        print("5. Story Mode (Campaign)")
        print("6. Exit")
        if canteen_unlocked:
            print("7. Canteen of the Heroes")

        choice = input("Choose an option: ").strip()
        if not choice.isdigit():
            print("Invalid option. Try again.")
            continue
        choice=int(choice)

        if choice==1:
            player=input("Trainer, enter your name: ")
            team_size=int(input("How many Pokémon will your team have? (1-3) "))
            while team_size < 1 or team_size > 3:
                team_size=int(input("How many Pokémon will your team have? (1-3) "))
            player_team=choose_team(player, team_size)
            print("\nChoose your gamemode!")
            print("1. Player vs. Player")
            print("2. Player vs. CPU")
            mode_input=input("Enter choice (1 or 2): ").strip()
            if not mode_input.isdigit() or int(mode_input) not in [1,2]:
                print_slowly("Invalid choice. Returning to menu.")
                continue
            mode=int(mode_input)
            if mode==1:
                opponent=input("Player 2 name: ")
                opponent_team=choose_team(opponent, team_size)
            else:
                opponent=random.choice(["Cynthia","Lance","Lorelei"])
                opponent_team=generate_cpu_team(team_size)
                print_slowly(f"Opponent: {opponent} with team {opponent_team}")
            print_slowly("\nLet the battle begin!")
            winner=battle_loop(player, player_team, opponent, opponent_team, mode_choice=mode)
            print_slowly(f"\n🏆 {winner} wins the battle! 🏆")
            input("Press Enter to return to the main menu...")
        elif choice==2:
            print_slowly("Rules: 1) Choose gamemode. 2) Choose team size. 3) Battle until all on one team faint.")
        elif choice==3:
            print_slowly("Game Mechanics: Turn-based. Weather & terrain settings. Different nature per game.")
        elif choice==4:
            print_slowly("""
                Matagal nang panahon, sa digital realm ng Pytheria Online… may nangyaring hindi inaasahan.
                Isang araw, bigla na lang nag-glitch ang buong server at nagising ang mga Pokémon
                na parang naka-overclock sabay naka-3-in-1 coffee.

                Lahat sila naging hyper, malakas, at kung minsan… nag-aattitude pa na parang may sariling WiFi.
                May kumakalat na tsismis na may nagpasabog daw ng ‘mysterious data energy’ sa Mt. Bugnut.exe.

                Dahil dito, pati mga Pidgeot nagiging overpowered—minsan lumilipad nang pabaliktad,
                minsan lumilipad palabas ng screen. Hindi rin sila sumusunod sa physics engine. Bahala sila sa buhay nila.

                Syempre, nagpanic ang mga players… lalo na nung nakita nilang
                nagla-livestream ang Snorlax sa gitna ng kalsada habang sumasayaw ng virtual hiphop.

                Para maresolba ang kaguluhan, nag-organize ang League Admins
                ng malaking digital tournament bago tuluyang mag-crash ang buong server.

                At dito papasok ka, Trainer—oo, ikaw na nagbabasa ngayon.
                Kailangan mong sumali para malaman kung sino ang pasaway na nagmo-mod sa mga Pokémon
                at nagpapakawala ng illegal power-ups.

                At syempre… baka manalo ka rin ng bragging rights at
                achievement badge, at siyempre—unlimited rice sa canteen ng Pytheria Online (virtual pero okay na rin).
                """)
        elif choice==5:
            player=input("Trainer, enter your name: ")
            team_size=int(input("How many Pokémon will your team have? (1-3) "))
            player_team=choose_team(player, team_size)
            story_mode(player, player_team)
            input("Press Enter to return to the main menu...")
        elif choice==7 and canteen_unlocked:
            canteen_of_the_heroes()
            input("Press Enter to return to the main menu...")
        elif choice==6:
            print_slowly("Goodbye, Trainer!")
            break
        else:
            print("Invalid option. Try again.")

#Game start
start_game()

#Credits
"""
-The programmers utilized AI for the debugging and optimization of the game.
-This game took inspiration from the popular game Pokémon.
-This game based most of their features from the tutorial of CtrlAultDelTutorial titled, Pokétext
"""
