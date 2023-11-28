class NodeTree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []


    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def rem_child(self, child):
        self.children.remove(child)
        

    def __str__(self):
        return f"{self.data}"

    def level_count(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = " " * 3 * self.level_count()

        prefix = spaces + "|_____" if self.parent else ""

        print(prefix + self.data)

        #if self.children
        if self.children:
            for child in self.children:
                child.print_tree()
        
def node_printer():
    root = NodeTree("Nepal (CEO)")
    

    cto = NodeTree("Chinmay (CTO)")
    
    root.add_child(cto)

    hr_head = NodeTree("Gels (HR Head)")
    root.add_child(hr_head)
    recruitement_head = NodeTree("Peter (Recruitemt Manager)")
    hr_head.add_child(recruitement_head)

    pol_manager = NodeTree("Waqas (Policy Manager)")
    hr_head.add_child(pol_manager)

    inf_head = NodeTree("Vishwa (Infrastucture Head)")
    cto.add_child(inf_head)
    #Add to Vishwa
    cloud_manager = NodeTree("Dhaval (Cloud Manager)")
    inf_head.add_child(cloud_manager)
    app_manager = NodeTree("Abhijit (App Manager)")
    inf_head.add_child(app_manager)

    #Add app head

    app_head = NodeTree("Aamir (Application Head)")
    cto.add_child(app_head)


    

    root.print_tree()

    return root


if __name__ == "__main__":
    node_printer()
    pass
    
        
