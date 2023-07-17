import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

class newListTree:
    from DataToList import DataToList
    def __init__(self, trees):
        self.trees = trees
        self.fig = make_subplots(rows=5, cols=4, shared_yaxes=True, horizontal_spacing=0.05)
        self.fig.print_grid()


    def buildTree(self, tree):
        if isinstance(tree, list):
            node = {'children': []}
            for child in tree:
                child_node = self.buildTree(child)
                if child_node is not None:
                    node['children'].append(child_node)
            return node
        else:
            return {'value': tree}

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

    def main(self):
        DataToList = self.DataToList()
        treeLst = DataToList.dataToList()
        #treeLst = [self.listToString(tree) for tree in treeLst]
        tree_visualizer = newListTree(treeLst)
        tree_visualizer.visualize_trees()

if __name__ == '__main__':
    DataToList = newListTree.DataToList()
    treeLst = DataToList.dataToList()
    newListTree(treeLst).main()
