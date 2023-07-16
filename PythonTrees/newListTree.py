import plotly.graph_objects as go
from plotly.subplots import make_subplots
class Visualize:
    '''def numNodes(tree):
        nodes = 0
        for char in tree:
            if char == '(':
                nodes = nodes + 1
        return nodes

    def immediateChildren(tree):
        children = 0
        count = 0
        for char in tree[2:]:
            if char == '(':
                count = count + 1
            elif char == ')':
                count = count - 1
            if count == 0:
                children = children + 1
        return children
    numVertices = numNodes(tree)
    immediateChildren = immediateChildren(tree)'''

    def __init__(self, trees):
        self.trees = trees
        self.fig = make_subplots(rows=1, cols=len(trees), shared_yaxes=True, horizontal_spacing=0.05)


    def buildTree(self, tree):
        node = {'children': []}
        child_str = ''
        level = 0
        for char in tree:
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

tree1 = '[travel services, [travel agents]], [rv parks], [bed & breakfast], [hotels], [airports]'
tree2 = '[a[b][c]]'
tree3 = ' ( ) '
tree4 = '(((()()))(()())(()))'
tree5 = ' ( )( ) '
trees = [tree1, tree2, tree1, tree2]
tree_visualizer = Visualize(trees)
tree_visualizer.visualize_trees()


''' treeDict1 = buildTree(tree1)
    treeDict2 = buildTree(tree2)
    assign_coordinates(treeDict1)
    assign_coordinates(treeDict2)

    fig = go.Figure()

    if treeDict1 is not None:
        add_trace(treeDict1)

    if treeDict2 is not None:
        add_trace(treeDict2)

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        hovermode='closest',
        plot_bgcolor='rgb(248,248,248)'
    )

    fig.show()'''