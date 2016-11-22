/*
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/copy-books-ii
@Language: Java
@Datetime: 16-11-14 23:48
*/

public class Solution {
    /**
     * @param n: an integer
     * @param times: an array of integers
     * @return: an integer
     */
    public int copyBooksII(int n, int[] times) {
        // write your code here
        int k = times.length;
        int[][] f = new int[2][n+1];
        for (int j = 0 ; j <= n; ++j) {
            f[0][j] = j * times[0];
        }
        for (int i = 1; i < k; ++i) {
            for (int j = 1; j <= n; ++j) {
                int a = i%2;
                int b = 1-a;
                
                f[a][j] = Integer.MAX_VALUE;
                for (int l = 0; l <= j; ++l) {
                    if (f[b][j-l] > times[i] * l) {
                        f[a][j] = Math.min(f[a][j], f[b][j-l]);
                    } else {
                        f[a][j] = Math.min(f[a][j], times[i] * l);
                        break;
                    }
                }
                
            }
        }
        return f[(k-1)%2][n];
    }
}