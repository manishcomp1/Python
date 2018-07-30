
import pdb
class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance 

    def __init__(self):
        """ Virtually private constructor. """

        #print "Singleton.__instance---",Singleton.__instance
        if Singleton.__instance != None:
	    print "Exception raised"
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
            print "Singleton.__instance---",Singleton.__instance
    


s = Singleton() # Ok
#Singleton() # will raise exception

print s

"""
s = Singleton.getInstance()
print s

s = Singleton.getInstance()
print s # will print the same instance as before

"""
