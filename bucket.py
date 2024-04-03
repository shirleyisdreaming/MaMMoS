import math

class Bucket:
    """Water bucket.
    
    Parameters
    ----------
    radius
        Radius in m.
    height
        Height in m.
    filling
        Filling fraction of the bucket (0 empty, 1 full). 
        Default filling fraction is 0.5.
    """
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self._filling = 0.5  # filling between 0 and 1, default is 0.5
        
        self.bucket_volume=math.pi * self.radius**2 * self.height
   
    @property
    def filling(self):
        return self._filling
    
    def fill(self, amount):
        """Add amount of water to bucket.
        
        Excess water is lost if the bucket is too small/full.

        Parameters
        ----------
        amount
            Amount of water in m^3.

        """
        
        if(amount<0):
            self._filling = 0
        else: 
            if self._filling * self.bucket_volume + amount >= self.bucket_volume:
               self._filling = 1
            else:
               self._filling = (self._filling*self.bucket_volume + amount) / self.bucket_volume

	
    @filling.deleter
    def filling(self):
        del self._filling
   




