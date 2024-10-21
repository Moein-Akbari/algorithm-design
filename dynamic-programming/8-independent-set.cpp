#include <bits/stdc++.h>
using namespace std;

class Node
{
private:
    int id;
    int selected;
    int notSelected;
    vector<Node *> children;

public:
    int getMaxIndependentSet() {
        return max(selected, notSelected);
    }
    void calculateMaxIndependentSet()
    {
        for (Node *child : children)
        {
            child->calculateMaxIndependentSet();
            selected += child->notSelected;
            notSelected += max(child->notSelected, child->selected);
        }
    }

    Node(int id)
    {
        this->id = id;
        selected = 1;
        notSelected = 0;
    }
    void addChild(Node *child)
    {
        children.push_back(child);
    }
};

vector<Node *> getTree(int n)
{
    vector<Node *> tree;
    for (int i = 0; i < n; i++)
        tree.push_back(new Node(i)); 

    for (int i = 0; i < n; i++)
        {
            int child;
            cin >> child;
            while (child != -1)
                tree[i]->addChild(tree[child]);
                cin >> child;
        }
    return tree;
}

int main()
{
    int n;
    cin >> n;
    vector<Node *> treeNodes = getTree(n);
    Node *tree = treeNodes[0];
    tree -> calculateMaxIndependentSet();
    cout << tree -> getMaxIndependentSet() << endl;
}