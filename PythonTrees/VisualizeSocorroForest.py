import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

class newListTree:
    from Forest import Forest
    from DataToList import DataToList
    def __init__(self, trees):
        self.trees = trees
        self.fig = make_subplots(rows=5, cols=4, shared_yaxes=True, horizontal_spacing=0.05)


    def buildTree(self, tree):
        """ if isinstance(tree, list):
            node = {'children': []}
            for child in tree:
                child_node = self.buildTree(child)
                if child_node is not None:
                    node['children'].append(child_node)
            return node
        else:
            return {'value': tree}"""
        node = {'value': tree[0], 'children': []}
        for child in tree[1:]:
            if isinstance(child, list):
                child_node = self.buildTree(child)
                if child_node is not None:
                    node['children'].append(child_node)
            else:
                node['children'].append({'value': child})
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
                    line=dict(color='rgb(210,210,210)', width=1),
                    hoverinfo='none',
                    showlegend=False,
                ), row=row, col=col)
                self.add_trace(child, row, col)
        
        self.fig.add_trace(go.Scatter(
            x=[node['x']],
            y=[node['y']],
            mode='markers',
            marker=dict(size=10, color='rgb(100,100,100)'),
            hoverinfo='none',
            showlegend=False,
        ), row=row, col=col)

    def visualize_trees(self):
        num_trees = len(self.trees)
        num_cols = 4  # Set the number of columns per row (adjust as needed)
        num_rows = math.ceil(num_trees / num_cols)

        for i, tree in enumerate(self.trees):
            tree_dict = self.buildTree(tree)
            self.assign_coordinates(tree_dict)
            row = (i // num_cols) + 1
            col = (i % num_cols) + 1
            self.add_trace(tree_dict, row=row, col=col)
            self.fig.update_xaxes(visible=False, showticklabels=False, row=row, col=col)
            self.fig.update_yaxes(visible=False, showticklabels=False, row=row, col=col)

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

    """    def main(self):
        DataToList = self.DataToList()
        treeLst = DataToList.dataToList()
        tree_visualizer = newListTree(treeLst)
        tree_visualizer.visualize_trees()"""

    def main(self):
        DataToList = self.DataToList()
        original = DataToList.dataToList()
        Forest = self.Forest()
        Forest.setForest(original)
        print("original forest:")
        print(original)

        treeList = []
        for i, tree in enumerate(original):
            treeList.append(self.listToString(tree))
        
        anonymousForest = Forest.anonymize_forest_greedy() 
        print("anonymous forest greedy: ")
        anonymousList = []
        for i, tree in enumerate(anonymousForest[0]):
            anonymousList.append(self.listToString(tree))
        print(anonymousList)
        print("pairs:")
        print(anonymousForest[2])
        print("Edit distance for anonymous Forest greedy:")
        print(anonymousForest[1])

        original = newListTree(treeList)
        original.visualize_trees()
        anonymized = newListTree(anonymousList)
        anonymized.visualize_trees()

if __name__ == '__main__':
        newListTree([[]]).main() 
        """niceForest = [
    ['hotels & travel', ['travel services', ['travel agents']], ['rv parks'], ['bed & breakfast'], 
        ['hotels'], ['airports']],
    ['religious organizations', ['churches']],
    ['automotive', ['gas stations'], ['truck rental', ['trailer rental']], ['body shop'],
        ['auto repair'], ['car dealers'], ['auto detailing'], ['auto parts']],
    ['arts & entertainment', ['rodeo']],
    ['health & medical', ['hospitals'], ['home health care'], ['physical therapy'], ['dentists'],
        ['counseling & mental health']],
    ['food', ['food trucks'], ['coffee & tea'], ['bakeries'], ['grocery'], ['farmers market']],
    ['nightlife', ['bars'], ['lounges']],
    ['public services & government', ['landmarks & historical buildings'], ['parks'], ['museums'], 
        ['police departments'], ['post offices']],       
    ['local services', ['cemeteries'], ['community service/non-profit'], ['shipping centers'], 
        ['forestry'], ['pest control'], ['funeral services & cemeteries'], ['community services/non-profit'],
        ['appraisal services']],
    ['restaurants', ['american (new)'], ['burgers'], ['breakfast & brunch', ['burgers', ['hot dogs']]],
        ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea']]], ['fast food', 
        ['burgers', ['ice cream & frozen yogurt']]], ['mexican'], ['pizza', ['fast food']], 
        ['pizza', ['chicken wings', ['sandwiches']]], ['sandwiches', ['fast food']]],
    ['pets', ['animal shelters'], ['veterinarians']],
    ['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts'], ['fashion', ["women's clothing"]],
        ['thrift stores'], ['home & garden', ['hardware stores']], ['home & garden'], ['art galleries'], 
        ['flea markets'], ['department stores']],
    ['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']],
    ['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']],
    ['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']],
    ['mass media ', ['radio stations'], ['print media']],
    ['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']],
    ['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents']], ['real estate ', ['property management']], ['real estate', ['home developers']], ['real estate', ['solar installation']]],
    ['beauty & spas']]"""
        """    greedy = Forest.anonymize_forest_greedy()
    bruteForce = Forest.anonymize_forest_brute_force()""""""    greedyViz = newListTree(greedy)
    greedyViz.main()

    bfViz = newListTree(bruteForce)
    bfViz.main()"""

