class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def level_count(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def rem_child(self, child):
        self.children.remove(child)

    def print_trees(self):
        spaces = " " * self.level_count() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                self.print_tree()

    def print_tree(self, level):
        if self.level_count() > level:
            return
        spaces = ' ' * self.level_count() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
                
    def print_kids(self):
        print(self.children)

    def __str__(self):
        return f"{self.data}"

    

def node_printer():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)
    
    root.print_tree(3)
    return root

if __name__ == "__main__":
    node_printer()
    pass
