// In the name of God

using namespace std;

#include <vector>
#include <iostream>
#include <set>
const int INF = 1e9;

class Node {
private:
    int id;
    bool _isSelected;
public:
    vector<pair<int, Node*>> neighbours;
    Node(int id){
        this -> id = id;
        this -> _isSelected = false;
    }
    void addNeighbour(Node* neighbour, int weight);
    void select() {_isSelected = true;}
    bool isSelected() {return _isSelected;}
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
    int vertex = 1;
    int mstWeight = 0;
    int parWeight[numberOfVertices];
    set<pair<int, int>> bestDistances; //<weight, vertex>

    int distances[numberOfVertices];
    for (int i = 0; i < numberOfVertices; ++i)
        distances[i] = INF;
    distances[vertex] = 0;

    vertices[vertex] -> select();
    int numberOfSelectedVertices = 1;
    while (numberOfSelectedVertices < this -> numberOfVertices) {
        cout << vertex << endl;
        for (pair<int, Node*> edge : vertices[vertex] -> neighbours) {
            int weight = edge.first;
            cout << "Weight:" << weight << endl;
            Node* neighbour = edge.second;
            cout << "neighbour: " << neighbour -> getId() << endl;
            if (distances[neighbour -> getId()] > distances[vertex] + weight) {
                distances[neighbour -> getId()] = distances[vertex] + weight;
                parWeight[neighbour -> getId()] = weight;
                bestDistances.erase(make_pair(distances[neighbour -> getId()], neighbour -> getId()));
                bestDistances.insert(make_pair(distances[vertex] + weight, neighbour -> getId()));
            }
        }
        cout << "out of for!" << endl;
        // Selecting next minimum vertex
        auto bestDistance = bestDistances.begin();
        vertex = (*bestDistance).second;

        // Skipping the vertex while it is selected.
        while (vertices[vertex] -> isSelected()){
            vertex = (*bestDistance).second;
            bestDistances.erase(*bestDistance);
            bestDistance = bestDistances.begin();
        }

        mstWeight += parWeight[vertex];
        vertices[vertex] -> select();
        numberOfSelectedVertices++;
        cout << "end of while " << vertex << endl;
    }
    for (int i = 0; i < numberOfVertices; i++)
        cout << parWeight[i] << ' ';
    cout << endl;
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