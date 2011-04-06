import breve
import os, sys

class myBraitenbergControl( breve.BraitenbergControl ):
    def __init__( self ):
        breve.BraitenbergControl.__init__( self )
        myBraitenbergControl.init( self )
    
    def init( self ):
        breve.myBraitenbergControl = myBraitenbergControl


#Create an instance of our controller object to initialize the simulation
myBraitenbergControl()
