class athlete():
    '''
    a class created to store athlete information requiring name,team, and sex to be able to accurately represent them
    due to weight being on a different table on lifting cast we cant have weight on init
    
    '''
       
    def __init__(self,name,team,sex):
        self.name = name
        self.team = team
        self.isMale = sex
        self.Class = 0
        self.weight = 0
        self.total = 0
        self.gl = 0
        self.bestSquat = 0
        self.bestDead = 0
        self.bestBench = 0
        
    def __repr__(self):
        return f"athlete(name'{self.name}',team = {self.team}', isMale = {self.isMale} , weight = {self.weight})"
        
    def setWeight(self,kgs):
        '''
        sets athletes weight and places them in their weight class
        '''
        self.weight = kgs
        self.setClass(kgs)
        
    def getWeight(self):
        '''
        returns the athletes bodyweight at weight ins
        '''
        return self.weight
    
    def setClass(self,kgs):
        '''
        sets athlete weight class depending on sex and weight in kgs
        if class will be set to high number for heavy weights
        
        o(n) time
        '''
        found = False
        paMClasses = [59,66,74,83,93,105,120,999]
        paFClasses = [47,52,57,63,72,84,998]
        weight = 0
        
        if self.isMale:
            while weight < len(paMClasses) and not found:
                if paMClasses[weight] > kgs:
                    found = True
                    weight = paMClasses[weight]
                else:
                    weight += 1
        else:#if theyre a women
            while weight < len(paFClasses) and not found:
                if paFClasses[weight] > kgs:
                    found = True
                    weight = paFClasses[weight]
                else:
                    weight += 1
        
        self.Class = weight
        
    def getClass(self):
        '''
        returns the athlete weight class
        '''
        return self.Class
    
    def getTotal(self):
        '''
        returns the total of the athlete
        '''
        total = self.bestBench+self.bestDead+self.bestSquat
        return total
    
    def updateBest(self,lift,attempt,isGood):
        """
        will change the bestlift depending on the lift and if the attempt was made
        Args:
            lift (str): describes what kind of lift is being made
            attempt (int): weight of the attempt
            isGood (bool): if the attempt was made
        """
        if isGood:
            match lift:
                case "dead":
                    self.bestDead = attempt
                case "bench":
                    self.bestBench = attempt
                case "squat":
                    self.bestSquat = attempt
                
            self.calcGlPts()
            
    def calcGlPts(self):
        weight = self.weight
        total = self.total
        sex = self.isMale
        a,b,c = 0
        
        if sex:
            a = 1199.72839
            b = -102.11299
            c = 0.0000022
        else:
            a = 1249.1533
            b = -123.9606
            c = 0.0000062
            
        bottom = a+b * weight + c * weight**2
        glPoints = (total/bottom) * 100
        self.gl = glPoints
        
    def getGl(self):
        return self.gl