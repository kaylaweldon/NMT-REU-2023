import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class TreeTesting{

    // Test various aspects of our trees
    public static void main(String[] args){

        // create test root and see if it has 0 children
        Node rootTest = new Node();
        System.out.printf("RootTest node has %d children \n", rootTest.getNumberOfChildren());

        // build test tree out of Nodes adding each manually
        Node root = new Node("1");
        //second level
        root.children.add(new Node("2"));
        root.children.add(new Node("3"));
        root.children.add(new Node("4"));
        //third level
        root.children.get(0).children.add(new Node("5"));
        root.children.get(0).children.add(new Node("6"));
        root.children.get(0).children.add(new Node("7"));
        root.children.get(1).children.add(new Node("8"));
        root.children.get(2).children.add(new Node("9"));
        root.children.get(2).children.add(new Node("10"));
        root.children.get(2).children.add(new Node("11"));
        //print tree
        printNAryTree(root);

        // build test tree out of Nodes by passing a list of children to constructor
        
        // create LinkedList of children to add to root
        List<Node> childrenToAdd = new LinkedList<Node>();

        // creates a list of Nodes like : <"5", "6", "7", "8", "9", "10", "11">
        for(int categoryToAdd = 5; categoryToAdd < 12; categoryToAdd++){
            String categoryAsString = Integer.toString(categoryToAdd);
            Node child = new Node(categoryAsString);
            childrenToAdd.add(categoryToAdd - 5, child);
        }

        // populate a CategoryTree with our list of children to add
        CategoryTree T1 = new CategoryTree("Salons");
        T1.getRoot().setChildren(childrenToAdd);

        // print T1
        printNAryTree(T1.getRoot());

    }

    // function to print the CategoryTree
    private static void printNAryTree(Node root){

        if(root == null) return;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {

            int length = queue.size();

            // so that we can reach each level
            for(int i = 0 ; i < length ; i++) { 

                Node node = queue.poll();
                System.out.print(node.getCategoryString() + " ");

                // for-Each loop to iterate over all children
                for (Node item : node.children) { 
                    queue.offer(item);
                }
            }

            System.out.println();

        }
}

}