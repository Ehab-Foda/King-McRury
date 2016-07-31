class Wall(): 
"""This class makes the basis for a wall model with max 6layers...
    the wall layers are assigned empty list to be...
    called by two arguments i.e. thickness and material"""
    def __init__(self, wall_type,layer1[],layer2[],layer3[],layer4[],layer5[], layer6[]):
    self.wall_type = wall_type
    self.layer1 = layer1[]
    self.layer2 = layer2[]
    self.layer3 = layer3[]
    self.layer4 = layer4[]
    self.layer5 = layer5[]
    self.layer6 = layer6[]
    def u_value_calc(self):
        """This method is to caluclate U-value for the wall layers without convection boundary in/out i.e. added later"""
