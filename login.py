
class user_data:
    def __init__(self,name,display_name,password):
        self.name=name
        self.display_name=display_name
        self.password=password
    def display_data(self):
        print(self.name,self.display_name,self.password)

