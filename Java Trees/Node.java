import java.util.LinkedList;
import java.util.List;

public class Node {

    // attributes
    private int numberOfChildren;
    private String categoryString;
    List<Node> children = new LinkedList<>();
    boolean isLeaf;

    // constructors

    // constructs Node with no children and empty categoryString
    public Node(){
        numberOfChildren = 0;
        String categoryString = "";
        isLeaf = true;
    }

    // constructs Node with specified category string and children
    public Node(String category, List<Node> childrenToAdd){
        categoryString = category;
        children = childrenToAdd;
        numberOfChildren = children.size();
        isLeaf = false;
    }

    // constructs Node with specified category string
    public Node(String category){
        categoryString = category;
        isLeaf = false;  
    }
   
    // getters
    public int getNumberOfChildren(){
        return numberOfChildren;
    }

    public String getCategoryString(){
        return categoryString;
    }

    // setters
    public void setCategoryString(String inputCategory){
        categoryString = inputCategory;
    }

    public void setChildren(List<Node> childrenToAdd){
        children = childrenToAdd;
    }


}