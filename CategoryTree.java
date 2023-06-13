public class CategoryTree extends Node{

    private Node root;
    private int numberOfLevels;
    private int numberOfNodes;

    // constructors
    public CategoryTree(){

        // constructs a tree with one node with no children
        root = new Node();
        numberOfLevels = 1;
        numberOfNodes = 1;

    }

    // maybe make anoter constructor where we can feed it a list? seems hard atm.
    // we can just manually build a tree like in the TreeTesting.java file

    // getters
    public int getNumberOfLevels(){
        return numberOfLevels;
    }

    public int getNumberOfNodes(){
        return numberOfNodes;
    }

}