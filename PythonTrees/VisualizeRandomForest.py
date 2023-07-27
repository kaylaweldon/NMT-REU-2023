import plotly.graph_objects as go
from plotly.subplots import make_subplots
class newListTree:
    from Forest import Forest
    def __init__(self, trees):
        self.trees = trees
        self.fig = make_subplots(rows=1, cols=len(trees), shared_yaxes=True, horizontal_spacing=0.05)


    def buildTree(self, tree):
        node = {'children':[]}
        child_str = ''
        level = 0
        for char in tree[1:]:
            if char == '[':
                level += 1
            elif char == ']':
                level -= 1
            if char == '[' and level == 1:
                child_str = ''
            elif char == ']' and level == 0:
                if child_str:
                    child = self.buildTree(child_str)
                    if child is not None:
                        node['children'].append(child)
                child_str = ''
            else:
                child_str += char
        return node


    def assign_coordinates(self, node, x=0, y=0, x_shift=1):
        node['x'] = x
        node['y'] = y
        if 'children' in node:
            total_children = len(node['children'])
            for i, child in enumerate(node['children']):
                x_child = x + (i - (total_children - 1) / 2) * x_shift
                self.assign_coordinates(child, x_child, y - 1, x_shift / total_children)

    def add_trace(self, node, row, col):
        if 'children' in node:
            for child in node['children']:
                self.fig.add_trace(go.Scatter(
                    x=[node['x'], child['x']],
                    y=[node['y'], child['y']],
                    mode='lines',
                    line=dict(color='black', width=1),
                    hoverinfo='none',
                    showlegend=False,
                ), row=row, col=col)
                self.add_trace(child, row, col)
        
        self.fig.add_trace(go.Scatter(
            x=[node['x']],
            y=[node['y']],
            mode='markers',
            marker=dict(
            color='white',
            size=50,
            line=dict(
                color='blue',
                width=8
            )
        ),
            hoverinfo='none',
            showlegend=False,
        ), row=row, col=col)

    def visualize_trees(self):
        for i, tree in enumerate(self.trees):
            tree_dict = self.buildTree(tree)
            self.assign_coordinates(tree_dict)
            subplot = (1, i + 1)
            row, col = subplot
            self.add_trace(tree_dict, row = row, col = col)
            self.fig.update_xaxes(visible=False, showticklabels=False, row=row, col=col)
            self.fig.update_yaxes(visible=False, showticklabels=False, row= row, col=col)
        
        self.fig.update_layout(
            hovermode='closest',
            plot_bgcolor='rgb(255,255,255)'
        )
        
        self.fig.show()
    def listToString(self, lst): 
        result = ""
        if isinstance(lst, list):
            result += "["
            for item in lst:
                result += self.listToString(item) + ", "
            result = result.rstrip(", ") + "]"
        else:
            result += str(lst)
        return result
    
    def print_and_append(self, text, file_path):
        print(text)
        with open(file_path, 'a') as file:
            file.write(text + '\n')

    def main(self):
        """   Forest = self.Forest()
        Forest.generate_forest(3, 4, 4)
        niceForest = Forest.__get_forest__()
        Forest.setForest(niceForest)
        print(niceForest)
        niceForest0 = self.listToString(niceForest[0])
        niceForest1= self.listToString(niceForest[1])
        niceForest2 = self.listToString(niceForest[2])
        niceForest = [niceForest0, niceForest1, niceForest2]
        tree_visualizer = newListTree(niceForest)
        tree_visualizer.visualize_trees()

        greedy = Forest.anonymize_forest_greedy()
        bf = Forest.anonymize_forest_brute_force()

        print(greedy)
        print(bf)

        greedy = self.listToString(greedy[0])
        bf = self.listToString(bf[0])

        tree_visualizer = newListTree(greedy)
        tree_visualizer.visualize_trees()
        tree_visualizer = newListTree(bf)
        tree_visualizer.visualize_trees()
        """

        log_file_path = "log.txt"  # Replace with the desired file path for your log

        Forest = self.Forest()
        #niceForest = [['a', ['x'], ['c', ['l']], ['d', ['l']]], ['b', ['e', ['f'], ['g']], ['h', ['i']]], ['a', ['b'], ['c'], ['d'], ['e'], ['f', ['g', ['h']], ['h']]],  ['a', ['b', ['c', ['d'], ['e', ['f']], ['g'] ]], ['g', ['h']]], ['z', ['a', ['z', ['l']]], ['b'], ['g'], ['c', ['d'], ['f']]], ['a', ['x'],['b', ['c', ['d', ['e', ['f']],['x'], ['x'], ['g']]], ['x']]]]
        niceForest = [['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], 
            ['hotels'], ['airports']],
        ['religious organizations', ['churches']], ['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'],
            ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']], ['arts & entertainment', ['rodeo']], ['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'],
            ['counseling & mental health']], ['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']], ['nightlife', ['bars'], ['lounges']], 
            ['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], 
            ['police departments'], ['post offices']], ['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], 
            ['forestry'], ['pest control'], ['funeral services & cemeteries'],
            ['appraisal services']], ['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]],
            ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ["breakfast & brunch"], ["burgers"]], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], 
            ['sandwiches', ['fast food']]], ['pets', ['animal shelters'], ['veterinarians']], ['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]],
            ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], 
            ['flea markets'], ['department stores']], ['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']], ['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']], ['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']],
            ['mass media ', ['radio stations'], ['print media']], ['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']], ['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]],
            ['beauty & spas']]

        Forest.setForest(niceForest)

        self.print_and_append("Original Forest:", log_file_path)
        self.print_and_append(str(niceForest), log_file_path)

        numNodesOg = Forest.number_of_nodes(niceForest)

        self.print_and_append("Num Nodes in the original forest:", log_file_path)
        self.print_and_append(str(numNodesOg), log_file_path)

        greedy = Forest.anonymize_forest_greedy()

        numNodesGreedy = Forest.number_of_nodes(greedy[0])
        self.print_and_append("Greedy:", log_file_path)
        self.print_and_append(str(greedy[0]), log_file_path)

        self.print_and_append("Num nodes in greedy:", log_file_path)
        self.print_and_append(str(numNodesGreedy), log_file_path)


        """lub = Forest.leastUpperBound(niceForest[0], niceForest[1])
        niceForest0 = newListTree.listToString(self, niceForest[0])
        niceForest1 = newListTree.listToString(self, niceForest[1])
        print("Random Tree 1:")
        print(niceForest[0])
        print("Random Tree 2:")
        print(niceForest[1])
        print("Common Tree & LUB:")
        print(lub)
        lubStr = newListTree.listToString(self, lub[0])
        treeList= [niceForest0, niceForest1, lubStr]
        tree_visualizer = newListTree(treeList)
        tree_visualizer.visualize_trees()"""

if __name__ == '__main__':
    newListTree([[]]).main()