import java.util.LinkedList;
import java.util.List;

public class Node {

    // attributes
    private int numberOfChildren;
    private String categoryString;
    List<Node> children = new LinkedList<>();
    boolean isLeaf;

    // constructors
    public Node(){
        numberOfChildren = 0;
        String categoryString = "";
        isLeaf = true;
    }

    public Node(String category, List<Node> childrenToAdd){
        categoryString = category;
        children = childrenToAdd;
        numberOfChildren = children.size();
        isLeaf = false;
    }

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


}