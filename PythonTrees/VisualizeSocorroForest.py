import plotly.graph_objects as go
from plotly.subplots import make_subplots

class newListTree:
    from Forest import Forest
    def __init__(self, trees):
        self.trees = trees    # list of trees to visualize
        self.fig = make_subplots(rows=5, cols=4, shared_yaxes=True, horizontal_spacing=0.05)

    # builds a tree-like dictionary from a given list
    def buildTree(self, tree):
        node = {'value': tree[0], 'children': []}
        for child in tree[1:]:
            if isinstance(child, list):
                child_node = self.buildTree(child)
                if child_node is not None:
                    node['children'].append(child_node)
            else:
                node['children'].append({'value': child})
        return node

    # assigns (x, y) coordinates to each node in the tree
    def assign_coordinates(self, node, x=0, y=0, x_shift=1):
        node['x'] = x
        node['y'] = y
        if 'children' in node:
            total_children = len(node['children'])
            for i, child in enumerate(node['children']):
                x_child = x + (i - (total_children - 1) / 2) * x_shift
                self.assign_coordinates(child, x_child, y - 1, x_shift / total_children)

    # adds traces for drawing each trees nodes and edges
    def add_trace(self, node, row, col):
        if 'children' in node:
            for child in node['children']:
                # adds a trace for the edge between parent and each child
                self.fig.add_trace(go.Scatter(
                    x=[node['x'], child['x']],
                    y=[node['y'], child['y']],
                    mode='lines',
                    line=dict(color='black', width=1),
                    hoverinfo='none',
                    showlegend=False,
                ), row=row, col=col)
                # recursively adds trace for children
                self.add_trace(child, row, col)
        #adds trace for current node
        self.fig.add_trace(go.Scatter(
            x=[node['x']],
            y=[node['y']],
            mode='markers',
            marker=dict(size=10, color='blue'),
            hoverinfo='none',
            showlegend=False,
        ), row=row, col=col)

    # calculates number of trees to be visualized and sets up the grid layout and number of columns
    def visualize_trees(self):
        num_cols = 4  # Set the number of columns per row (adjust as needed)

        # iterate through each tree and visualize it in a subplot
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


    def main(self):
        Forest = self.Forest()
        niceForest = [
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
            ['forestry'], ['pest control'], ['funeral services & cemeteries'],
            ['appraisal services']],
        ['restaurants', ['american (new)', ['steakhouses', ['seafood']]], ['burgers', ['fastfood']], ['breakfast & brunch', ['burgers', ['hot dogs']]],
            ['chinese', ['buffets']], ['fast food', ['burgers', ['coffee & tea'], ['ice cream & frozen yogurt']]], ['mexican', ["breakfast & brunch"], ["burgers"]], ['pizza', ['fast food'], ['chicken wings', ['sandwiches']]], 
            ['sandwiches', ['fast food']]],
        ['pets', ['animal shelters'], ['veterinarians']],
        ['shopping', ['discount stores'], ['mobile phones'], ['flowers & gifts', ['gift shops']], ['fashion', ["women's clothing"]],
            ['thrift stores'], ['home & garden', ['hardware stores'], ['furniture stores']], ['art galleries'], 
            ['flea markets'], ['department stores']],
        ['education', ['middle & high schools'], ['elementary schools'], ['colleges & universities']],
        ['active life', ['swimming pools'], ['fitness & instructions', ['gyms']], ['golf']],
        ['financial services', ['banks & credit unions'], ['tax services'], ['insurance'], ['title loans']],
        ['mass media ', ['radio stations'], ['print media']],
        ['professional services', ['advertising'], ['web design'], ['business consulting'], ['accountants'], ['bookkeepers'], ['lawyers']],
        ['home services', ['plumbing'], ['utilities', ['electricity suppliers']], ['real estate', ['real estate agents'], ['property management'], ['home developers'], ['solar installation']]],
        ['beauty & spas']]

        Forest.setForest(niceForest)

        print("Original:")
        print(niceForest)

        """anonymousForestGreedy = Forest.anonymize_forest_greedy() 
        print("anonymous forest greedy: ") 
        print(anonymousForestGreedy)"""

        anonymousForestBF = Forest.anonymize_forest_brute_force()
        print("anonymous forest brute force:")
        print(anonymousForestBF)

        original = newListTree(niceForest)
        original.visualize_trees()
        
        """anonGreedy = newListTree(anonymousForestGreedy[0])
        anonGreedy.visualize_trees()"""
        anonBf = newListTree(anonymousForestBF[0])
        anonBf.visualize_trees()

if __name__ == '__main__':
        newListTree([[]]).main() 

