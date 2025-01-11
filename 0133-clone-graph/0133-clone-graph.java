/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbours;

    public Node(){
        val = 0;
        neighbours = new ArrayList<Node>();
    }

    public Node(int _val){
        val = _val;
        neighbours = new ArrayList<Node>();
    }

    public Node(int _val, ArrayList<Node> _neighbours){
        val = _val;
        neighbours = _neighbours;
    }
}

*/

class Solution {

    private Node dfs(Node node, Map<Node,Node> oldToNew){

        if(node==null){
            return null;
        }

        if(oldToNew.containsKey(node)){
            return oldToNew.get(node);
        }

        Node copy = new Node(node.val);
        oldToNew.put(node, copy);

        for(Node nei: node.neighbors){
            copy.neighbors.add(dfs(nei, oldToNew));
        }

        return copy;

    }

    public Node cloneGraph(Node node) {
        Map<Node, Node> oldToNew = new HashMap<>();
        return dfs(node, oldToNew);
    }
}