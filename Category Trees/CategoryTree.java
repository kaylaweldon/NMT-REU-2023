public class CategoryTree {

    private Node root;
    private int numberOfLevels;
    private int numberOfNodes;
    private String category;

    // constructors
    public CategoryTree(){

        // constructs a tree with one node with no children
        root = new Node();
        numberOfLevels = 1;
        numberOfNodes = 1;
        category = "newCategory";

    }

    public CategoryTree(String desiredCategoryString){

        // constructs a tree with one node, no children, and category label
        root = new Node(desiredCategoryString);
        numberOfLevels = 1;
        numberOfNodes = 1;
        category = desiredCategoryString;

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

    public String getCategory() {
        return category;
    }

    public Node getRoot(){
        return root;
    }

    // sort nodes at level from least children to most children 
    public void sortLevel(int level){

    }

}