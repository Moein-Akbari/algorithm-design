#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
const int MAX = 1e6 + 5;

vector<long long> factorial(MAX), inv_fact(MAX);

long long power(long long x, long long y, long long p) {
    long long res = 1;
    x = x % p;
    while (y > 0) {
        if (y & 1)
            res = (res * x) % p;
        y = y >> 1;
        x = (x * x) % p;
    }
    return res;
}

void precompute() {
    factorial[0] = 1;
    for (int i = 1; i < MAX; i++) {
        factorial[i] = (factorial[i - 1] * i) % MOD;
    }
    inv_fact[MAX - 1] = power(factorial[MAX - 1], MOD - 2, MOD);
    for (int i = MAX - 2; i >= 0; i--) {
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
    }
}

long long choosing(int n, int k) {
    if (k > n || k < 0) return 0;
    return (factorial[n] * inv_fact[k] % MOD) * inv_fact[n - k] % MOD;
}

vector<int> two_section(vector<vector<int>>& adjacency_list) {
    int n = adjacency_list.size();
    vector<int> sections(n, -1);
    queue<int> q;
    sections[0] = 0;
    q.push(0);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adjacency_list[u]) {
            if (sections[v] == -1) {
                sections[v] = 1 - sections[u];
                q.push(v);
            } else if (sections[v] == sections[u]) {
                return {};
            }
        }
    }
    return sections;
}

long long with_odd_ways(int n, int edges, int k) {
    long long possible_edges = (static_cast<long long>(n) * (n - 1) / 2) - edges;
    return choosing(possible_edges, k) * factorial[k] % MOD;
}

long long without_odd_ways(int section1_size, int section2_size, int edges, int k) {
    long long e11 = choosing(section1_size, 2); 
    long long e12 = choosing(section2_size, 2); 
    long long sum_edge_two_sections = (e11 + e12) % MOD; 
    long long edges_between_two_sections = (static_cast<long long>(section1_size) * section2_size) - edges; 
    long long ans = 0;

    for (int i = 1; i <= k; i++) { 
        if (i > sum_edge_two_sections) break;
        if (k - i > edges_between_two_sections) continue;

        ans = (ans + choosing(sum_edge_two_sections, i) * choosing(edges_between_two_sections, k - i) % MOD * factorial[k]) % MOD;
    }
    return ans;
}

int main() {
    precompute(); 

    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<int>> adjacency_list(n);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        adjacency_list[u].push_back(v);
        adjacency_list[v].push_back(u);
    }

    vector<int> sections = two_section(adjacency_list);
    if (sections.empty()) {
        cout << with_odd_ways(n, m, k) << endl;
    } else {
        int section1_size = count(sections.begin(), sections.end(), 0);
        int section2_size = n - section1_size;
        cout << without_odd_ways(section1_size, section2_size, m, k) << endl;
    }

    return 0;
}