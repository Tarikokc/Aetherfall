import json

class Skill:
    
    with open("../skills_data.json", 'r', encoding='utf-8') as f:
        _skills_data= json.load(f)
        
    def __init__(self, name, skill_type, damage, cost, cooldown=0, effect_duration = 0,effect = None):
        self.name = name                    
        self.skill_type = skill_type        
        self.damage = damage                
        self.cost = cost                    
        self.cooldown = cooldown            
        self.current_cooldown = 0    
        self.effect_duration = effect_duration
        self.effect = effect
       

    def verify_cooldown(self,caster) : 
        return self.current_cooldown == 0 and caster.stamina >= self.cost
    
    def use_skill(self,caster,target) : 
        
        caster.stamina -= self.cost
        
        if self.skill_type == "physical" : 
            damage_target = max(0, self.damage + self.attack - target.defense)
            target.pv -= damage_target
            print(damage_target)
        elif self.skill_type == "magic":
            target.pv -= self.damage
        elif self.skill_type == "buff":
            if self.effect == "defense_up":
                caster.apply_buff("defense", 50, self.effect_duration)
            elif self.effect == "dodge_up":
                caster.apply_buff("dodge", 30, self.effect_duration)
        self.current_cooldown = self.cooldown
        return True

    def create(classe, name):
        """Créer une compétence depuis le JSON"""
        data = classe._skills_data[name]
        return classe(
            name=name,
            skill_type=data["skill_type"],
            damage=data["damage"],
            cost=data["cost"],
            cooldown=data["cooldown"],
            effect=data.get("effect"),
            effect_duration=data["effect_duration"]
        )



        
        