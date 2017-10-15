#!/usr/local/bin/python
import LinAlg

def firelaser(atom):
	
    Atom.spin_update()
    Atom.xyplane_update()

def generate_location(atom):
    Atom..mvMult(['Atom.atom_plane'] [ 1, 1 ,1] )
     


class Atom():
    def __init__(self,name):
        self.name = name
	self.atom_plane = [ 0, 0, 0 ]
	self.spin = ''
	self.Ek = ''
	self.Ep = ''

    def spin_update(self):
        self.spin = 'z'

    def xyplane_update(self):
        self.atom_plane[0]=''
        self.atom_plane[1]=''
        self.atom_plane[2]=''


        
o2_1 = Atom('o2_1') 

print o2_1.spin

o2_1.spin_update()
o2_1.xyplane_update()

print 'debug'+ o2_1.spin
print 'debug'+ str(o2_1.atom_plane[0:3])


