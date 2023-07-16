import plotly.graph_objects as go
from plotly.subplots import make_subplots
class newListTree:
    from Forest import Forest
    from DataToList import DataToList
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
                    line=dict(color='rgb(210,210,210)', width=1),
                    hoverinfo='none',
                    showlegend=False,
                ), row=row, col=col)
                self.add_trace(child, row, col)
        
        self.fig.add_trace(go.Scatter(
            x=[node['x']],
            y=[node['y']],
            mode='markers',
            marker=dict(size=15, color='rgb(100,100,100)'),
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

    def main(self):
        Forest = self.Forest()
        Forest.generate_forest(4, 4, 4)
        niceForest = Forest.__get_forest__()
        lub = Forest.leastUpperBound(niceForest[0], niceForest[1])
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
        tree_visualizer.visualize_trees()
        
        """DataToList = self.DataToList()
        treeLst = DataToList.dataToList()
        treeLst = newListTree.listToString(self, treeLst)
        tree_visualizer = newListTree(treeLst)
        tree_visualizer.visualize_trees()"""

if __name__ == '__main__':
    newListTree([[]]).main()