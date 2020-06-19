        self.swap_item()
        self.move_right()
        print(self.compare_item())
        while self.move_right():
            # print(self.compare_item())
            if self.compare_item() == 1:
                # print("switched item")
                self.swap_item()
            # print("moved right")
        
        while self.move_left() and self.compare_item() != none:
            print("moved left")
            print(self._position)
            print(self.compare_item())
            if self.compare_item() == None:
                self.swap_item
                print(l)