public class CategoryTree extends Node{

    private Node root;
    private int numberOfLevels;
    private int numberOfNodes;

    // constructors
    public Tree(){

        // constructs a tree with one node with no children
        root = new Node();
        numberOfLevels = 1;
        numberOfNodes = 1;

    }

}