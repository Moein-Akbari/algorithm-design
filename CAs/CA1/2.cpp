#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int minimumImpacts(int n, int m) {
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (i == 1)
                dp[i][j] = j;
            else if (j == 1)
                dp[i][j] = 1;
            else {
                int low = 1, high = j, best = j;
                while (low <= high) {
                    int mid = (low + high) / 2;
                    int breaks = dp[i - 1][mid - 1];
                    int noBreak = dp[i][j - mid];
                    int worstCase = 1 + max(breaks, noBreak);
                    
                    best = min(best, worstCase);
                    
                    if (breaks > noBreak)
                        high = mid - 1;
                    else
                        low = mid + 1;
                }
                dp[i][j] = best;
            }
        }
    }
    
    return dp[n][m];
}

int main() {
    int n, m;
    cin >> n >> m;    
    cout << minimumImpacts(n, m) << endl;
    return 0;
}
