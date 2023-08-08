import numpy as np
from . import *

def perseverationsList(l):
    """One line description here.
    
        Detailed description here. Detailed description here.  Detailed 
        description here.  
    
        Args:
            arg1 (type): Description here.
            arg2 (type): Description here.
        Returns:
            Detailed description here. Detailed description here.  Detailed 
            description here. 
    """
    if len(l) > 0:
        return (
            [perseverationsList(i) for i in l]
            if isinstance(l[0][0], list)
            else [
                list({item for item in ls if ls.count(item) > 1}) for ls in l
            ]
        )
    else:
        return []


def perseverations(l):
    """One line description here.
    
        Detailed description here. Detailed description here.  Detailed 
        description here.  
    
        Args:
            arg1 (type): Description here.
            arg2 (type): Description here.
        Returns:
            Detailed description here. Detailed description here.  Detailed 
            description here. 
    """
    def processList(l2):
        return [float(len(i)-len(set(i))) for i in l2]
    
    # if fluency data are hierarchical, report mean per individual
    if isinstance(l[0][0],list):
        return [np.mean(processList(subj)) for subj in l]
    # if fluency data are non-hierarchical, report mean per list
    else:
        return processList(l)
