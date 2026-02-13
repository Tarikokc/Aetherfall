class Status():    
    def __init__(self, duration, value=0):
        self.duration = duration
        self.value = value
    
    
class Poison(Status):    
    def __init__(self, duration=3, damage=15):
        super().__init__(duration, damage)
    
    def apply(self, target):
        target.pv -= self.value
        print(f"{target.name} perd {self.value} PV de poison")
    
    def get_name(self):
        return "Poison"


class Shield(Status):    
    def __init__(self, duration=3, absorption=50):
        super().__init__(duration, absorption)
    
    def apply(self, target):
        pass 
    
    def absorb_damage(self, damage):
        absorbed = min(damage, self.value)
        self.value -= absorbed

        if self.value <= 0:
            self.duration = 0  
        
        return damage - absorbed
    
    def get_name(self):
        return f"Bouclier ({self.value})"


class Stun(Status):    
    def __init__(self):
        super().__init__(duration=1)
    
    def apply(self, target):
        print(f"{target.name} est étourdi")
    
    def get_name(self):
        return "Stun"
