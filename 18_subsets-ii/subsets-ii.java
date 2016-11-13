/*
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/subsets-ii
@Language: Java
@Datetime: 15-06-22 21:38
*/

class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public ArrayList<ArrayList<Integer>> subsetsWithDup(ArrayList<Integer> S) {
        // write your code here
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> list = new ArrayList<Integer>();
        if(S.isEmpty() || S == null) {
            return result;
        }
        Collections.sort(S);
        subsetsHelper(result, list, S, 0);

        return result;
    }
    
     private void subsetsHelper(ArrayList<ArrayList<Integer>> result,
        ArrayList<Integer> list, ArrayList<Integer> num, int pos) {

        result.add(new ArrayList<Integer>(list));
        
        for (int i = pos; i < num.size(); i++) {
            if ( i != pos && num.get(i) == num.get(i - 1)) {
                continue;
            }    
            list.add(num.get(i));
            subsetsHelper(result, list, num, i + 1);
            list.remove(list.size() - 1);
        }
    }
}

