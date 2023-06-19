from Node import Node
from Visualize import Visualize
from ete3 import Tree, TreeStyle

#t = Tree('A', ('B', 'E', 'F', ('H', 'I')), 'C', 'D')


t = Tree( "((a,b),c);" )
t.render("mytree.png", w=183, units="mm")

