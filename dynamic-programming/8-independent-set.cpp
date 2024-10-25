#include <bits/stdc++.h>
using namespace std;

class Node
{
private:
    int id;
    bool isSelected;
    int selected;
    int notSelected;
    vector<Node *> children;

public:
    int getMaxIndependentSet() {
        return max(selected, notSelected);
    }

    bool getIsSelected(){
        return isSelected;
    }

    int getId(){
        return id;
    }

    void selectionCheck(bool isParentSelected = false){
        isSelected = false;
        if (!isParentSelected && selected > notSelected)
            isSelected = true;

        for (auto child: children)
            child->selectionCheck(isSelected);
    }

    void calculateMaxIndependentSet()
    {
        for (Node *child : children)
        {
            child->calculateMaxIndependentSet();
            selected += child->notSelected;

            if (child->notSelected > child->selected)
                notSelected += child->notSelected;
            else
                notSelected += child->selected;
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
        while (child != -1){
            tree[i]->addChild(tree[child]);
            cin >> child;
        }
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

    tree ->selectionCheck();
    for (auto child: treeNodes)
        if (child->getIsSelected())
            cout << child->getId() << " " ;
}

/*
12
1 2 3 -1
4 5 6 -1
7 -1
-1
-1
8 9 -1
-1
10 11 -1
-1
-1
-1
-1
*/