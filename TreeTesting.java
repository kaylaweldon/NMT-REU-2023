import java.util.LinkedList;
import java.util.Queue;

public class TreeTesting{

    // Test various aspects of our trees
    public static void main(String[] args){

        Node rootTest = new Node();

        System.out.printf("RootTest node has %d children \n", rootTest.getNumberOfChildren());

        Node root = new Node("1");
        root.children.add(new Node("2"));
        root.children.add(new Node("3"));
        root.children.add(new Node("4"));
        root.children.get(0).children.add(new Node("5"));
        root.children.get(0).children.add(new Node("6"));
        root.children.get(0).children.add(new Node("7"));
        root.children.get(1).children.add(new Node("8"));
        root.children.get(2).children.add(new Node("9"));
        root.children.get(2).children.add(new Node("10"));
        root.children.get(2).children.add(new Node("11"));
        printNAryTree(root);

    }

    private static void printNAryTree(Node root){
        if(root == null) return;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int len = queue.size();
            for(int i=0;i<len;i++) { // so that we can reach each level
                Node node = queue.poll();
                System.out.print(node.getCategoryString() + " ");
                for (Node item : node.children) { // for-Each loop to iterate over all childrens
                    queue.offer(item);
                }
            }
            System.out.println();
        }
}

}