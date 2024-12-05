import pygame
import random


class Freddy:
    def __init__(self, FredAgg, jump):
        self.CurrLoc = 0
        self.FredAgression = FredAgg
        self.FreddyAI = 0
        self.jump = jump
        self.last_attempt = pygame.time.get_ticks()
        self.move_delay = 3000
        self.move_chance = 0
        self.door_time = None
        self.jumpscare_triggered = False
        self.jumpscare_delay = 5000
    def AI(self, Rdoorstage, screen, menuactive):
        current_time = pygame.time.get_ticks()
        if self.jump == 0:
            if current_time - self.last_attempt >= self.move_delay:
                self.move_chance = random.randint(1, 10)

                if self.move_chance <= self.FredAgression and self.CurrLoc < 8:
                    if self.CurrLoc == 1:
                        self.FreddyAI = random.choice([2, 3])  
                    elif self.CurrLoc == 3:
                        self.FreddyAI = 1
                    elif self.FreddyAI < 4:
                        self.FreddyAI += 1
                    elif self.FreddyAI < 4:
                        self.FreddyAI += 1 
                    
                self.move_chance = 0
                self.last_attempt = current_time

        if self.FreddyAI == 0: 
            self.CurrLoc = 0
        if self.FreddyAI == 1: 
            self.CurrLoc = 1
        if self.FreddyAI == 2:
            self.CurrLoc = 3
        if self.FreddyAI == 3: 
            self.CurrLoc = 7
        if self.FreddyAI == 4:
            self.CurrLoc = 8
        

        if self.FreddyAI > 4:
            self.FreddyAI = 4

        if self.CurrLoc == 8:
            if Rdoorstage == 0:
                if self.door_time is None:
                    self.door_time = pygame.time.get_ticks()
                elif current_time - self.door_time >= self.jumpscare_delay and not self.jumpscare_triggered:
                    self.trigger_jumpscare(screen, menuactive)
            else:
                self.door_time = None
                self.FreddyAI = 0
    def trigger_jumpscare(self, screen, menuactive):
        self.jump = 1
        self.jumpscare_triggered = True
        Jumpscare(screen, self.jump, menuactive)

class Bonnie:
    def __init__(self, BonAgg, jump):
        self.CurrLoc = 0
        self.BonAgression = BonAgg
        self.BonnieAI = 0
        self.jump = jump
        self.last_attempt = pygame.time.get_ticks()
        self.move_delay = 3000
        self.move_chance = 0
        self.door_time = None
        self.jumpscare_triggered = False
        self.jumpscare_delay = 5000
    def AI(self, Ldoorstage, screen, menuactive):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_attempt >= self.move_delay:
            self.move_chance = random.randint(1, 10)
            if self.jump == 0:
                if self.move_chance <= self.BonAgression and self.CurrLoc < 8:
                    if self.CurrLoc == 1:  # If Bonnie is in the dining room
                        self.BonnieAI = random.choice([2, 3])  
                    elif self.CurrLoc == 2:  # If Bonnie is in the Parts and service
                        self.BonnieAI = 1  # Move back to the dining room
                    elif self.CurrLoc == 3: #If Bonnie is in the Left Hall
                        self.BonnieAI = random.choice([4, 5]) 
                    elif self.CurrLoc == 6: #If Bonnie is in the Storage Closet
                        self.BonnieAI = 3
                    elif self.BonnieAI < 4:
                        self.CurrLoc += 1  # Regular movement increment
                    elif self.BonnieAI < 4:
                        self.BonnieAI += 1  
                self.move_chance = 0
                self.last_attempt = current_time

        if self.BonnieAI == 0: #Stage
            self.CurrLoc = 0
        if self.BonnieAI == 1: # Dine
            self.CurrLoc = 1
        if self.BonnieAI == 2: # Parts and Service
            self.CurrLoc = 2
        if self.BonnieAI == 3: # Left Hall
            self.CurrLoc = 5
        if self.BonnieAI == 4: # Storage Closet
            self.CurrLoc = 6
        if self.BonnieAI == 5: # Left Door
            self.CurrLoc = 8
        

        if self.BonnieAI > 5:
            self.BonnieAI = 5
        
        if self.CurrLoc == 8:
            if Ldoorstage == 0:
                if self.door_time is None:
                    self.door_time = pygame.time.get_ticks()
                elif current_time - self.door_time >= self.jumpscare_delay and not self.jumpscare_triggered:
                    self.trigger_jumpscare(screen, menuactive)
            else:
                self.door_time = None
                self.BonnieAI = 0
    def trigger_jumpscare(self, screen, menuactive):
        self.jump = 2
        self.jumpscare_triggered = True
        Jumpscare(screen, self.jump, menuactive)

class Chica:
    def __init__(self, ChicaAgg, jump):
        self.CurrLoc = 0
        self.ChicaAgression = ChicaAgg
        self.ChicaAI = 0
        self.jump = jump
        self.last_attempt = pygame.time.get_ticks()
        self.move_delay = 3000
        self.move_chance = 0
        self.door_time = None
        self.jumpscare_triggered = False
        self.jumpscare_delay = 5000
    def AI(self, Rdoorstage, screen, menuactive):
        current_time = pygame.time.get_ticks()
        if self.jump == 0:
            if current_time - self.last_attempt >= self.move_delay:
                self.move_chance = random.randint(1, 10)
                if self.move_chance <= self.ChicaAgression and self.CurrLoc < 8:
                    if self.ChicaAI < 4:
                        self.ChicaAI += 1  
                self.move_chance = 0
                self.last_attempt = current_time

        if self.ChicaAI == 0: #Stage
            self.CurrLoc = 0
        if self.ChicaAI == 1: # Dine
            self.CurrLoc = 1
        if self.ChicaAI == 2: # Right Hall
            self.CurrLoc = 7
        if self.ChicaAI == 3: # Right Door
            self.CurrLoc = 8
        

        if self.ChicaAI > 3:
            self.ChicaAI = 3

        if self.CurrLoc == 8:
            if Rdoorstage == 0:
                if self.door_time is None:
                    self.door_time = pygame.time.get_ticks()
                elif current_time - self.door_time >= self.jumpscare_delay and not self.jumpscare_triggered:
                    self.trigger_jumpscare(screen, menuactive)
            else:
                self.door_time = None
                self.ChicaAI = 0
    def trigger_jumpscare(self, screen, menuactive):
        self.jump = 3
        self.jumpscare_triggered = True
        Jumpscare(screen, self.jump, menuactive)
   
class Foxy:
    def __init__(self, FoxyAgg, jump):
        self.CurrLoc = 4
        self.FoxAgression = FoxyAgg
        self.FoxAI = 0 
        self.jump = jump
        self.last_attempt = pygame.time.get_ticks()
        self.move_delay = 3000
        self.move_chance = 0
        self.door_time = None
        self.jumpscare_triggered = False
        self.jumpscare_delay = 4000

    def AI(self, Ldoorstage, screen, menuactive):
        current_time = pygame.time.get_ticks()
        if self.jump == 0:
            if current_time - self.last_attempt >= self.move_delay:
                self.move_chance = random.randint(1, 10)
                if self.move_chance <= self.FoxAgression and self.CurrLoc < 8:
                    if self.FoxAI < 4:
                        self.FoxAI += 1  
                self.move_chance = 0
                self.last_attempt = current_time

        if self.FoxAI == 0: #Cove Curtain Closed
            self.CurrLoc = 4
        elif self.FoxAI == 1: #Peeking Curtain
            self.CurrLoc = 4
        elif self.FoxAI == 2: #In the open
            self.CurrLoc = 4
        elif self.FoxAI == 3: #Leaves Cove and appears in hall
            self.CurrLoc = 5
        elif self.FoxAI == 4: #In Doorway
            self.CurrLoc = 8


        if self.FoxAI > 4:
            self.FoxAI = 4
        if self.CurrLoc == 8:
            if Ldoorstage == 0:
                if self.door_time is None:
                    self.door_time = pygame.time.get_ticks()
                elif current_time - self.door_time >= self.jumpscare_delay and not self.jumpscare_triggered:
                    self.trigger_jumpscare(screen, menuactive)
            else:
                self.door_time = None
                self.FoxAI = 0

    def trigger_jumpscare(self, screen, menuactive):
        self.jump = 4
        self.jumpscare_triggered = True
        Jumpscare(screen, self.jump, menuactive)



            

class ShareAnimatronic:
    def __init__(self, foxy, freddy, bonnie, chica):
        self.foxy = foxy
        self.freddy = freddy
        self.bonnie = bonnie
        self.chica = chica

    def LocationUpdate(self, stagecam, dinecam, rhallcam, lhallcam, rerocam, pscam, pccam, sccam, BG_officeL, BG_officeR):
    # Stage
        try:
            if self.freddy.CurrLoc == 0 and self.bonnie.CurrLoc == 0 and self.chica.CurrLoc == 0:
                stagecam = pygame.image.load("Stage1.png")
            elif self.freddy.CurrLoc == 0 and self.bonnie.CurrLoc == 0:
                stagecam = pygame.image.load("StageFredBon.png")
            elif self.bonnie.CurrLoc == 0 and self.chica.CurrLoc == 0:
                stagecam = pygame.image.load("StageBonChi.png")
            elif self.freddy.CurrLoc == 0 and self.chica.CurrLoc == 0:
                stagecam = pygame.image.load("StageFredChi.png")
            elif self.freddy.CurrLoc == 0:
                stagecam = pygame.image.load("StageFred.png")
            elif self.bonnie.CurrLoc == 0:
                stagecam = pygame.image.load("StageBon.png")
            elif self.chica.CurrLoc == 0:
                stagecam = pygame.image.load("StageChi.png")
            else:
                stagecam = pygame.image.load("StageNone.png")
            
        except FileNotFoundError as e:
            stagecam = pygame.Surface((1920, 1080))
            stagecam.fill((100, 100, 100)) 
    # Dining Room
        try:
            if self.freddy.CurrLoc == 1 and self.bonnie.CurrLoc == 1 and self.chica.CurrLoc == 1:
                dinecam = pygame.image.load("DineAll.png")
            elif self.freddy.CurrLoc == 1 and self.bonnie.CurrLoc == 1:
                dinecam = pygame.image.load("DineFredBon.png")
            elif self.bonnie.CurrLoc == 1 and self.chica.CurrLoc == 1:
                dinecam = pygame.image.load("DineBonChi.png")
            elif self.freddy.CurrLoc == 1 and self.chica.CurrLoc == 1:
                dinecam = pygame.image.load("DineFredChi.png")
            elif self.freddy.CurrLoc == 1:
                dinecam = pygame.image.load("DineFred.png")
            elif self.bonnie.CurrLoc == 1:
                dinecam = pygame.image.load("DineBon.png")
            elif self.chica.CurrLoc == 1:
                dinecam = pygame.image.load("DineChi.png")
            else:
                dinecam = pygame.image.load("Dine1.png")
            
        except FileNotFoundError as e:
            dinecam = pygame.Surface((1920, 1080))
            dinecam.fill((100, 100, 100)) 
    #Parts and Service
        try:
            if self.bonnie.CurrLoc == 2:
                pscam = pygame.image.load("PSBon.png")
            else:
                pscam = pygame.image.load("PS1.png")
            
        except FileNotFoundError as e:
            pscam = pygame.Surface((1920, 1080))
            pscam.fill((100, 100, 100)) 
    # Restroom
        try:
            if self.freddy.CurrLoc == 3:
                rerocam = pygame.image.load("RestroomFred.png")
            else:
                rerocam = pygame.image.load("Restroom1.png")
            
        except FileNotFoundError as e:
            rerocam = pygame.Surface((1920, 1080))
            rerocam.fill((100, 100, 100)) 
    # Pirate Cove
        try:
            if self.foxy.FoxAI == 0:
                pccam = pygame.image.load("Cove1.png")
            elif self.foxy.FoxAI == 1:
                pccam = pygame.image.load("Cove2.png")
            elif self.foxy.FoxAI == 2:
                pccam = pygame.image.load("Cove3.png")
            elif self.foxy.FoxAI >= 3:
                pccam = pygame.image.load("Cove4.png")
            else:
                raise ValueError(f"Unexpected FoxAI value: {self.foxy.FoxAI}")
            
        except (FileNotFoundError, ValueError) as e:
            pccam = pygame.Surface((1920, 1080)) 
            pccam.fill((0, 0, 0))
    # Left Hall 
        try:
            if self.foxy.CurrLoc == 5 and self.bonnie.CurrLoc == 5:
                lhallcam = pygame.image.load("LHallBonFox.png")
            elif self.foxy.CurrLoc == 5:
                lhallcam = pygame.image.load("LHallFox.png")
            elif self.bonnie.CurrLoc == 5:
                lhallcam = pygame.image.load("LHallBon.png")
            else:
                lhallcam = pygame.image.load("LHall1.png")
            
        except FileNotFoundError as e:
            lhallcam = pygame.Surface((1920, 1080))
            lhallcam.fill((100, 100, 100)) 
    # Storage Closet
        try:
            if self.bonnie.CurrLoc == 6:
                sccam = pygame.image.load("ClosetBon.png")
            else:
                sccam = pygame.image.load("Closet1.png")
        except FileNotFoundError as e:
            sccam = pygame.Surface((1920, 1080))
            sccam.fill((100, 100, 100)) 
    # Right Hallway
        try:
            if self.freddy.CurrLoc == 7 and self.chica.CurrLoc == 7:
                rhallcam = pygame.image.load("RHallFredChi.png")
            elif self.freddy.CurrLoc == 7:
                rhallcam = pygame.image.load("RHallFred.png")
            elif self.chica.CurrLoc == 7:
                rhallcam = pygame.image.load("RHallChi.png")
            else:
                rhallcam = pygame.image.load("RHall1.png")
            
        except FileNotFoundError as e:
            lhallcam = pygame.Surface((1920, 1080))
            lhallcam.fill((100, 100, 100)) 
    # Left Doorway
        try:
            if self.foxy.CurrLoc == 8:
                BG_officeL = pygame.image.load("OfficeL_Foxy.png")
            elif self.bonnie.CurrLoc == 8:
                BG_officeL = pygame.image.load("OfficeL_Bon.png")
            else:
                BG_officeL = pygame.image.load("BG_OfficeL.png")
            
        except FileNotFoundError as e:
            BG_officeL = pygame.Surface((1920, 1080))
            BG_officeL.fill((100, 100, 100))
    # Right Doorway
        try:
            if self.freddy.CurrLoc == 8:
                BG_officeR = pygame.image.load("OfficeR_Fred.png")
            elif self.chica.CurrLoc == 8:
                BG_officeR = pygame.image.load("OfficeR_Chi.png")
            else:
                BG_officeR = pygame.image.load("BG_OfficeR.png")
            
        except FileNotFoundError as e:
            BG_officeR = pygame.Surface((1920, 1080))
            BG_officeR.fill((100, 100, 100))
        

        return stagecam, dinecam, rhallcam, lhallcam, rerocam, pscam, pccam, sccam, BG_officeL, BG_officeR


            

class GameClock:
    def __init__(self, start_hour=12, start_minute=00, end_hour=6, speed=1000):
        self.hour = start_hour
        self.minute = start_minute
        self.end_hour = end_hour
        self.speed = speed
        self.last_update = pygame.time.get_ticks() 
        self.running = True

    def update_time(self, jump=0):
        if jump != 0:
            return
        if not self.running:
            return
        
        current_time = pygame.time.get_ticks()
        
        if current_time - self.last_update >= self.speed:
            self.minute += 1
            self.last_update = current_time

            if self.minute >= 60:
                self.minute = 0
                self.hour += 1


            if self.hour == self.end_hour:
                self.running = False

    def get_time(self):
        return f"{self.hour % 12 or 12}:{self.minute:02d} AM"


pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("One Night at Freddy's")

def main():
    clock = pygame.time.Clock()
    active = True
    menuactive = True
    officeactive = False
    customizeactive = False
    

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active = False

        if menuactive:
            menuactive, officeactive, customizeactive = menu(screen)

        if customizeactive:
            customizeactive, FreddyaggressionLevel, BonnieaggressionLevel, ChicaaggressionLevel, FoxyaggressionLevel, officeactive = customize(screen)

        if officeactive:
            office(screen, FreddyaggressionLevel, BonnieaggressionLevel, ChicaaggressionLevel, FoxyaggressionLevel)

        if officeactive == False and menuactive == False:
            menuactive = GameOver(screen, menuactive)


        clock.tick(60)

    pygame.quit()

def menu(screen):
    menuactive = True
    officeactive = False
    customizeactive = False
    menuImage = pygame.image.load("BG_Menu.png")

    while menuactive:
        screen.blit(menuImage, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_RETURN:
                    menuactive = False
                    customizeactive = True

    return menuactive, officeactive, customizeactive

def customize(screen):
    customizeactive = True
    officeactive = False
    FreddyaggressionLevel = 0
    BonnieaggressionLevel = 0
    ChicaaggressionLevel = 0
    FoxyaggressionLevel = 0
    currentanimatronicselect = 1
    pygame.font.init()
    font = pygame.font.Font(None, 64)

    instructions = [
        "Use the Right and Left Arrow keys to adjust aggression levels.",
        "Press ENTER to start the night.",
        "Use the Up and Down Arrow keys to select an Animatronic"
    ]
    last_key_time = pygame.time.get_ticks()
    key_delay = 200  

    while customizeactive:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                current_time = pygame.time.get_ticks()

                if current_time - last_key_time > key_delay:
                    if event.key == pygame.K_RETURN:
                        customizeactive = False
                        officeactive = True
                    elif event.key == pygame.K_RIGHT:
                        if currentanimatronicselect == 1:
                            FreddyaggressionLevel = min(FreddyaggressionLevel + 1, 10)
                        elif currentanimatronicselect == 2:
                            BonnieaggressionLevel = min(BonnieaggressionLevel + 1, 10)
                        elif currentanimatronicselect == 3:
                            ChicaaggressionLevel = min(ChicaaggressionLevel + 1, 10)
                        elif currentanimatronicselect == 4:
                            FoxyaggressionLevel = min(FoxyaggressionLevel + 1, 10)
                    elif event.key == pygame.K_LEFT:
                        if currentanimatronicselect == 1:
                            FreddyaggressionLevel = max(FreddyaggressionLevel - 1, 0)
                        elif currentanimatronicselect == 2:
                            BonnieaggressionLevel = max(BonnieaggressionLevel - 1, 0)
                        elif currentanimatronicselect == 3:
                            ChicaaggressionLevel = max(ChicaaggressionLevel - 1, 0)
                        elif currentanimatronicselect == 4:
                            FoxyaggressionLevel = max(FoxyaggressionLevel - 1, 0)
                    elif event.key == pygame.K_UP:
                        currentanimatronicselect = max(currentanimatronicselect - 1, 1)
                    elif event.key == pygame.K_DOWN:
                        currentanimatronicselect = min(currentanimatronicselect + 1, 4)

                    last_key_time = current_time

        freddy_color = (0, 255, 0) if currentanimatronicselect == 1 else (255, 255, 255)
        bonnie_color = (0, 255, 0) if currentanimatronicselect == 2 else (255, 255, 255)
        chica_color = (0, 255, 0) if currentanimatronicselect == 3 else (255, 255, 255)
        foxy_color = (0, 255, 0) if currentanimatronicselect == 4 else (255, 255, 255)

        freddy_text = font.render(f"Freddy Aggression: {FreddyaggressionLevel}", True, freddy_color)
        bonnie_text = font.render(f"Bonnie Aggression: {BonnieaggressionLevel}", True, bonnie_color)
        chica_text = font.render(f"Chica Aggression: {ChicaaggressionLevel}", True, chica_color)
        foxy_text = font.render(f"Foxy Aggression: {FoxyaggressionLevel}", True, foxy_color)

        screen.blit(freddy_text, (50, 100))
        screen.blit(bonnie_text, (50, 200))
        screen.blit(chica_text, (50, 300))
        screen.blit(foxy_text, (50, 400))

        for i, line in enumerate(instructions):
            instruction_text = font.render(line, True, (200, 200, 200))
            screen.blit(instruction_text, (50, 500 + i * 40))

        pygame.display.flip()

    return customizeactive, FreddyaggressionLevel, BonnieaggressionLevel, ChicaaggressionLevel, FoxyaggressionLevel, officeactive



def office(screen,  FreddyaggressionLevel, BonnieaggressionLevel, ChicaaggressionLevel, FoxyaggressionLevel):
    officeactive = True
    menuactive = False
    camactive = 0
    jump = 0 
    currCam = 0
    BG_officeL = pygame.image.load("BG_OfficeL.png")
    BG_officeR = pygame.image.load("BG_OfficeR.png")
    buttonR = pygame.image.load("ButtonR01.png")
    buttonL = pygame.image.load("ButtonL01.png")
    doorL_open = pygame.image.load("DoorLOpen.png")
    doorR_open = pygame.image.load("DoorROpen.png")
    doorL_close = pygame.image.load("DoorLClosed.png")
    doorR_close = pygame.image.load("DoorRClosed.png")
    camflipbutton = pygame.image.load("CamButton.png")
    Rdoorstage = 0
    Ldoorstage = 0
    stagecam = pygame.image.load("Stage1.png")
    dinecam = pygame.image.load("Dine1.png")
    rhallcam = pygame.image.load("RHall1.png")
    lhallcam = pygame.image.load("LHall1.png")
    rerocam = pygame.image.load("Restroom1.png")
    pscam = pygame.image.load("PS1.png")
    pccam = pygame.image.load("Cove1.png")
    sccam = pygame.image.load("Closet1.png")
    cammap = pygame.image.load("CamMap0.png")
    BonAgg = BonnieaggressionLevel 
    FredAgg = FreddyaggressionLevel
    ChicaAgg = ChicaaggressionLevel
    FoxyAgg = FoxyaggressionLevel
    freddy = Freddy(FredAgg, jump)
    foxy = Foxy(FoxyAgg, jump)
    bonnie = Bonnie(BonAgg, jump)
    chica = Chica(ChicaAgg, jump)
    movelocations = ShareAnimatronic(foxy, freddy, bonnie, chica)
    game_clock = GameClock(speed=2000)
    pygame.font.init()
    font = pygame.font.Font(None, 64) 
    GOScene = False
    GWScene = False
    doorL = doorL_open
    doorR = doorR_open
    while officeactive:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if camactive == 0:
                    if buttonL_Collide.collidepoint(event.pos):
                        Ldoorstage = (Ldoorstage + 1) % 2
                        doorL, doorR = DoorToggle(Ldoorstage, Rdoorstage, doorL_close, doorL_open, doorR_close, doorR_open)
                    if buttonR_Collide.collidepoint(event.pos):
                        Rdoorstage = (Rdoorstage + 1) % 2
                        doorL, doorR = DoorToggle(Ldoorstage, Rdoorstage, doorL_close, doorL_open, doorR_close, doorR_open)
                if camflip_Collide.collidepoint(event.pos):
                    camactive = (camactive + 1) % 2

            if event.type == pygame.KEYDOWN:
                if camactive == 1:
                    if event.key == pygame.K_RIGHT:
                        currCam = (currCam + 1) % 8
                    elif event.key == pygame.K_LEFT:
                        currCam = (currCam - 1) % 8
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            
        
        
        stagecam, dinecam, rhallcam, lhallcam, rerocam, pscam, pccam, sccam, BG_officeL, BG_officeR = movelocations.LocationUpdate(stagecam, dinecam, rhallcam, lhallcam, rerocam, pscam, pccam, sccam, BG_officeL, BG_officeR)


        
        buttonR_Collide = buttonR.get_rect(topleft=(875, 110))
        buttonR_Collide = buttonR_Collide.inflate(-1825, -890)

        buttonL_Collide = buttonL.get_rect(topleft=(-860, 110))
        buttonL_Collide = buttonL_Collide.inflate(-1840, -890)

        camflip_Collide = camflipbutton.get_rect(topleft=(0,480))
        camflip_Collide = camflip_Collide.inflate(-940,-959)
        screen.blit(camflipbutton, camflip_Collide.topleft)

        
        if camactive == 0:
            screen.blit(BG_officeL, (0, 0))
            screen.blit(BG_officeR, (0, 0))
            screen.blit(doorL, (0, 0))
            screen.blit(doorR, (0, 0))
            screen.blit(buttonR, (0,0))
            screen.blit(buttonL, (0,0))
            screen.blit(camflipbutton, (0,0))


        else:
            if currCam == 0:
                screen.blit(stagecam, (0,0))
                cammap = pygame.image.load("CamMapStage.png")
            elif currCam == 1:
                screen.blit(dinecam, (0,0))
                cammap = pygame.image.load("CamMapDine.png")
            elif currCam == 2:
                screen.blit(pscam, (0,0))
                cammap = pygame.image.load("CamMapPS.png")
            elif currCam == 3:
                screen.blit(rerocam, (0,0))
                cammap = pygame.image.load("CamMapRestroom.png")
            elif currCam == 4:
                screen.blit(pccam, (0,0))
                cammap = pygame.image.load("CamMapPCove.png")
            elif currCam == 5:
                screen.blit(lhallcam, (0,0))
                cammap = pygame.image.load("CamMapLHall.png")
            elif currCam == 6:
                screen.blit(sccam, (0,0))
                cammap = pygame.image.load("CamMapStoreClos.png")
            elif currCam == 7:
                screen.blit(rhallcam, (0,0))
                cammap = pygame.image.load("CamMapRHall.png")
            screen.blit(cammap, (0, 0))
            screen.blit(camflipbutton, (0,0))

        game_clock.update_time(jump=jump)
        current_time = game_clock.get_time()
        time_text = font.render(current_time, True, (255, 255, 255))

        freddy.AI(Rdoorstage, screen, menuactive)
        foxy.AI(Ldoorstage, screen, menuactive)
        bonnie.AI(Ldoorstage, screen, menuactive)
        chica.AI(Rdoorstage, screen, menuactive)


        if jump == 0:
            text_rect = time_text.get_rect()
            text_rect.topright = (screen.get_width() - 20, 20)
            screen.blit(time_text, text_rect.topleft)
        if jump > 1:
            officeactive = False 
        game_clock.update_time()


        pygame.display.update()
        if game_clock.running == False:
                officeactive = False  
                menuactive = GameWin(screen, menuactive)

    if officeactive:
        office(screen)
def DoorToggle(Ldoorstage, Rdoorstage, doorL_close, doorL_open, doorR_close, doorR_open):
    if Ldoorstage == 0:
        doorL = doorL_open
    else:
        doorL = doorL_close

    if Rdoorstage == 0:
        doorR = doorR_open
    else:
        doorR = doorR_close

    return doorL, doorR

def Jumpscare(screen, jump, menuactive):
    menuactive = GameOver(screen, menuactive)
    return menuactive

    
            

def GameWin(screen, menuactive):
    WinScene = True
    GameWinScreen = pygame.image.load("6AM.png")

    while WinScene:
        screen.blit(GameWinScreen, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    WinScene = False  
                    menuactive = True 
                    main()

    return menuactive

def GameOver(screen, menuactive):
    GOScene = True
    GameOverScreen = pygame.image.load("GameOver.png")
    while GOScene:
        screen.blit(GameOverScreen, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    GOScene = False
                    menuactive = True
                    main()
    return menuactive 




if __name__ == "__main__":
    main()