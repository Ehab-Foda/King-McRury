class Material():
    """This class makes the basis for a material data"""
    def __init__(self, name, roughness,thickness, conductivity, density, heat_capacity, thermal_absorptance, solar_absorptance, visible_absorptance):
    	self.name = name
    	self.roughness = roughness
    	self.thickness = thickness
    	self.conductivity = conductivity
    	self.density = density
    	self.heat_capacity = heat_capacity
    	self.thermal_absorptance = thermal_absorptance
    	self.solar_absorptance = solar_absorptance
    	self.visible_absorptance = visible_absorptance
    
    def diffusivity_calc(self):
        diffusivity = float()
        diffusivity = self.conductivity/(self.density*self.heat_capacity)
        return diffusivity
