class Atom:
    def __init__(self,atomtype,x,y,z):
        self.atomtype = atomtype
        self.position = (x,y,z)

    def __repr__(self):
        return f"Atom : {self.atomtype} at {self.position}"

    
print([Atom(atomtype,x,y,z) for (atomtype,x,y,z) in datapoint_list]]