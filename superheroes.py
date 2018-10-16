from random import randint


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    
    def attack(self):
        # Calculate lowest attack value as an integer.
        lowest = int(self.attack_strength) // 2
        # Use random.randint(a, b) to select a random attack value.
        highest = int(self.attack_strength)
        attack_val = randint(lowest, highest)
        # Return attack value between 0 and the full attack.
        return attack_val

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength

class Hero:
    def make_stats(self):
        print("Hero Kills: {}".format(self.kills))
        print("Hero Death: {}".format(self.deaths))

        if self.deaths > 0:
            print(int(self.kills) // int(self.deaths))

        else:
            print(int(self.kills))

    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
        self.weapons = list()

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense. 
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        total = 0

        for armor in self.armors:
            total += armor.defend()

        if self.health == 0:
            return 0

        return total

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the 
        hero's health. 
        If the hero dies update number of deaths.
        """
        if self.health > 0:
            self.health = self.health - damage_amt

            if self.health <= 0:
                self.deaths += 1
                return 1

        return 0


    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills = num_kills

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
    # Call the attack method on every ability in our ability list
        total = 0
        
        for ability in self.abilities:
            total += ability.attack()

        return total
    # Add up and return the total of all attacks

class Weapon(Ability):
    
    def attack(self):
        lowest = int(self.attack_strength) // 2
        highest = int(self.attack_strength)
        attack_val = randint(lowest, highest)
        # Return attack value between 0 and the full attack.
        return attack_val

class Team():

    def __init__(self, team_name):
        #Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        #"""Add Hero object to heroes list."""
        self.heroes.append(hero)

    def remove_hero(self, name):
       # """
       # Remove hero from heroes list.
       # If Hero isn't found return 0.
        #"""
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return self.heroes
            else:
                return 0

    def find_hero(self, name):
       # """
        #Find and return hero from heroes list.
       # If Hero isn't found return 0.
       # """
       for hero in self.heroes:
            if hero.name == name:
                return hero
            else:
                return 0

    def view_all_heroes(self):
       # """Print out all heroes to the console."""
       print (self.heroes)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """
        team_attack = 0

        for hero in self.heroes:
            team_attack += hero.attack()
        
        kills = other_team.defend(team_attack)

        for hero in self.heroes:
            hero.add_kill(kills)



    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        Return number of heroes killed in attack.
        """
        team_defense = 0

        for hero in self.heroes:
            team_defense += hero.defend()
     
        if damage_amt > team_defense:
            remainder = damage_amt - team_defense
            
            return self.deal_damage(remainder)
            
    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        dam_per_hero = damage//len(self.heroes)
        kills = 0

        for hero in self.heroes:
            kills += hero.take_damage(dam_per_hero)

        return kills

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health

    def check_heroes(self):
        for hero in self.heroes:
            if hero.health > 0:
                return True
        return False

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen. 
        This data must be output to the terminal.
        """
        for hero in self.heroes:
            hero.make_stats()
    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for hero in self.heroes:
            hero.add_kill()
class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the 
        initialized defend strength.
        """
        return randint(0, int(self.defense))

class Arena:
    def __init__(self):
        """
        Declare variables
        """
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        name = input("Enter a name for team one. ")
        self.team_one = Team(name)
        pick_hero = True

        while pick_hero:
            hero_name = input("Give your hero a name. ")
            hero = Hero(hero_name, health = 100)
            add_ab = input("Add an ability to this hero? Enter Y(yes) or N(no) ")

            if add_ab.lower() == 'y':
                abilities = True
            else:
                abilities = False

            while abilities:
                ab_name = input("Enter a name for the ability. ")
                ab_power = input('Give {} a power level. '.format(ab_name))

                if int(ab_power) > 300:
                    print('Invalid entry. Power levels must be numbers no greater than 300 ')
                else:
                    ab_power = ab_power

                ability = Ability(ab_name, ab_power)
                hero.add_ability(ability)
                again = input('Does this hero have more abilities? Enter Y(yes) or N(no) ')

                if again.lower() == 'y':
                    abilities = True
                else:
                    abilities = False
            
            add_wp = input('Does this hero have any weapons? Enter Y(yes) or N(no) ')
            
            if add_wp.lower() == 'y':
                pick_wp = True
            else:
                pick_wp = False

            while pick_wp:
                wp_name = input("What is the name of this weapon? ")
                wp_power = input('Give {} a power level. '.format(wp_name))

                if int(wp_power) > 300:
                    print('Invalid entry. Power levels must be numbers no greater than 300 ')
                else:
                    wp_power = wp_power

                weapon = Weapon(wp_name, wp_power)
                hero.add_weapon(weapon)
                again2 = input('Does this hero have another weapon? Enter Y(yes) or N(no) ')

                if again2.lower() == 'y':
                    pick_wp = True
                else:
                    pick_wp = False

            add_arm = input('Does this hero have any armor? Enter Y(yes) or N(no) ')
            
            if add_arm.lower() == 'y':
                pick_arm = True
            else:
                pick_arm = False

            while pick_arm:
                arm_name = input("What is the name of this armor? ")
                arm_power = input('Give {} a power level. '.format(arm_name))

                if int(arm_power) > 300:
                    print('Invalid entry. Power levels must be numbers no greater than 300 ')
                else:
                    arm_power = arm_power

                armor = Armor(arm_name, arm_power)
                hero.add_armor(armor)
                again3 = input('Does this hero have more armor? Enter Y(yes) or N(no) ')

                if again3.lower() == 'y':
                    pick_arm = True
                else:
                    pick_arm = False

            self.team_one.add_hero(hero)
            print("{} added to team {}. ".format(hero_name, name))
            again4 = input('Add another hero to your team? Enter Y(yes) or N(no) ')

            if again4.lower() == 'y':
                pick_hero = True
            else:
                pick_hero = False

        return self.team_one

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        name = input("Enter a name for team two. ")
        self.team_two = Team(name)
        pick_hero = True

        while pick_hero:
            hero_name = input("Give your hero a name. ")
            hero = Hero(hero_name, health = 100)
            add_ab = input("Add an ability to this hero? Enter Y(yes) or N(no) ")

            if add_ab.lower() == 'y':
                abilities = True
            else:
                abilities = False

            while abilities:
                ab_name = input("Enter a name for the ability. ")
                ab_power = input('Give {} a power level. '.format(ab_name))

                if int(ab_power) > 300:
                    print('Invalid entry. Power levels must be numbers no greater than 300 ')
                else:
                    ab_power = ab_power

                ability = Ability(ab_name, ab_power)
                hero.add_ability(ability)
                again = input('Does this hero have more abilities? Enter Y(yes) or N(no) ')

                if again.lower() == 'y':
                    abilities = True
                else:
                    abilities = False
            
            add_wp = input('Does this hero have any weapons? Enter Y(yes) or N(no) ')
            
            if add_wp.lower() == 'y':
                pick_wp = True
            else:
                pick_wp = False

            while pick_wp:
                wp_name = input("What is the name of this weapon? ")
                wp_power = input('Give {} a power level. '.format(wp_name))

                if int(wp_power) > 300:
                    print('Invalid entry. Power levels must be numbers no greater than 300')
                else:
                    wp_power = wp_power

                weapon = Weapon(wp_name, wp_power)
                hero.add_weapon(weapon)
                again2 = input('Does this hero have another weapon? Enter Y(yes) or N(no) ')

                if again2.lower() == 'y':
                    pick_wp = True
                else:
                    pick_wp = False

            add_arm = input('Does this hero have any armor? Enter Y(yes) or N(no) ')
            
            if add_arm.lower() == 'y':
                pick_arm = True
            else:
                pick_arm = False

            while pick_arm:
                arm_name = input("What is the name of this armor? ")
                arm_power = input('Give {} a power level. '.format(arm_name))

                if int(arm_power) > 300:
                    print('Invalid entry. Power levels must be numbers no greater than 300 ')
                else:
                    arm_power = arm_power

                armor = Armor(arm_name, arm_power)
                hero.add_armor(armor)
                again3 = input('Does this hero have more armor? Enter Y(yes) or N(no) ')

                if again3.lower() == 'y':
                    pick_arm = True
                else:
                    pick_arm = False

            self.team_two.add_hero(hero)
            print("{} added to team {}.".format(hero_name, name))
            again4 = input('Add another hero to your team? Enter Y(yes) or N(no) ')

            if again4.lower() == 'y':
                pick_hero = True
            else:
                pick_hero = False

        return self.team_two

    def team_battle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """
        battle = True
        
        while battle:
            team_one_status = self.team_one.check_heroes()
            team_two_status = self.team_two.check_heroes()

            if team_one_status and team_two_status:
                self.team_one.attack(self.team_two)
                self.team_two.attack(self.team_one)
            else:
                battle = False

    def show_stats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """
        print('{} statistics:\n\n'.format(self.team_one.name))
        
        self.team_one.stats()

        print('__________________________________________________')

        print('{} statistics:\n\n'.format(self.team_two.name))
        
        self.team_two.stats()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
