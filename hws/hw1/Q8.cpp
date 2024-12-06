#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> Rectangle(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = m - 1; j >= 0; j--) {
            // از سمت راست بالا وارد و از سمت چپ پایین خارج می‌شویم
            cin >> Rectangle[i][j];
        }
    }
    vector<vector<int>> lowest_cost(n, vector<int>(m));
    if (n > 0) {
        // مقداردهی سطر اول
        //  هزینه رسیدن به هر ایالت برابر هزینه رسیدن به ایالت سمت راست به علاوه مالیات ایالت است
        lowest_cost[0][0] = Rectangle[0][0];
        for (int i = 1; i < m; i++) {
            lowest_cost[0][i] = lowest_cost[0][i-1] + Rectangle[0][i];
        }
    }
    if (n > 1) {
        // مقداردهی سطر دوم
        //  هزینه رسیدن به هر ایالت برابر کمینه هزینه رسیدن به ایالت بالا و سمت راست آن، به علاوه مالیات ایالت است
        lowest_cost[1][0] = Rectangle[0][0] + Rectangle[1][0];
        for (int i = 1; i < m; i++) {
            lowest_cost[1][i] = min(lowest_cost[0][i], lowest_cost[1][i-1]) + Rectangle[1][i];
        }
    }
    if (n > 2) {
        // مقداردهی باقی سطرها
        //  هزینه رسیدن به هر ایالت برابر کمینه هزینه رسیدن به ایالت بالا، سمت راست و سمت چپ آن، به علاوه مالیات ایالت است
        for (int i = 2; i < n; i++) {
            // هزینه رسیدن به ایالت سمت چپ را نداریم. در ابتدا فقط هزینه رسیدن به ایالت را باتوجه به هزینه ایالت سمت راست و بالا محاسبه می‌کنیم
            lowest_cost[i][0] = lowest_cost[i-1][0] + Rectangle[i][0];
            for (int j = 1; j < m; j++) {
                lowest_cost[i][j] = min(lowest_cost[i-1][j], lowest_cost[i][j-1]) + Rectangle[i][j];
            }
            // حالا با مینیمم گرفتن بین هزینه محاسبه شده در مرحله قبل و هزینه ایالت سمت چپ به علاوه مالیات ایالت به جواب نهایی می‌رسیم
            for (int j = m - 2; j >= 0; j--) {
                lowest_cost[i][j] = min(lowest_cost[i][j], lowest_cost[i][j+1] +   Rectangle[i][j]);
            }
        }
    }
    cout << lowest_cost[n-1][m-1] << endl;
    return 0;
}