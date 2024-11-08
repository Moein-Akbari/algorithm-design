// In the name of God

using namespace std;

#include <vector>
#include <iostream>
#include <set>

class Node {
private:
    int id;
    bool isSelected;
public:
    vector<pair<int, Node*>> neighbours;
    Node(int id){
        this -> id = id;
        this -> isSelected = false;
    }
    void addNeighbour(Node* neighbour, int weight);
    void select() {isSelected = true;}
    int getId() {return id;}
};

void Node::addNeighbour(Node* neighbour, int weight) {
    neighbours.push_back(make_pair(weight, neighbour));
}

class Graph {
private:
    int numberOfVertices;
    vector<Node*> vertices;
    vector<pair<int, int>> mstEdges; //<vertex, vertex>
public:
    Graph(int numberOfVertices) {
        this -> numberOfVertices = numberOfVertices;
        for (int i = 0; i < numberOfVertices; i++)
            vertices.push_back(new Node(i));
    }
    void addEdge(int vertex1, int vertex2, int weight);

    int minimumSpanningTree();
};

void Graph::addEdge(int vertex1, int vertex2, int weight) {
    vertices[vertex1] -> addNeighbour(vertices[vertex2], weight);
    vertices[vertex2] -> addNeighbour(vertices[vertex1], weight);
}

int Graph::minimumSpanningTree() {
    set<pair<int, int>> bestDistances; //<weight, vertex>
    int distances[numberOfVertices];
    int vertex = 0;
    int mstWeight = 0;
    vertices[vertex] -> select();
    int numberOfSelectedVertices = 1;
    while (numberOfSelectedVertices < this -> numberOfVertices) {
        cout << vertex << endl;
        for (pair<int, Node*> edge : vertices[vertex] -> neighbours) {
            int weight = edge.first;
            Node* neighbour = edge.second;
            cout << "neighbour: " << neighbour -> getId() << endl;
            if (distances[neighbour -> getId()] > distances[vertex] + weight) {
                bestDistances.erase(make_pair(distances[neighbour -> getId()], neighbour -> getId()));
                bestDistances.insert(make_pair(distances[vertex] + weight, neighbour -> getId()));
            }
        }
        cout << "out of for!" << endl;
        auto bestDistance = bestDistances.begin();
        vertex = (*bestDistance).second;
        mstWeight += (*bestDistance).first;
        vertices[vertex] -> select();
        numberOfSelectedVertices++;
        bestDistances.erase(bestDistance);
        cout << "end of while" << endl;
    }
    return mstWeight;
}

int main() {
    Graph graph = Graph(9);
    vector<vector<int>> edges = {
        {0, 1 ,4},
        {0, 7, 8},
        {1, 7, 11},
        {1, 2, 8},
        {7, 8, 7},
        {7, 6, 1},
        {8, 6, 6}, 
        {8, 2, 2},
        {6, 5, 2},
        {5, 2, 4}, 
        {5, 3, 14},
        {5, 4, 10},
        {2, 3, 7},
        {3, 4, 9},
    };
    for (auto edge : edges) {
        graph.addEdge(edge[0], edge[1], edge[2]);
    }
    cout << graph.minimumSpanningTree() << endl;
}