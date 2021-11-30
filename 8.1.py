class Giraffes:
    def left_foot_forward(self):
        print ('Ліва нога спереді')
    def left_foot_back(self):
        print ('Ліва нога ззаді')
    def right_foot_forward(self):
        print ('Права нога спереді')
    def right_foot_back(self):
        print ('Права нога ззаді')
    def dancer(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_forward()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
reginald = Giraffes()
reginald.dancer()
