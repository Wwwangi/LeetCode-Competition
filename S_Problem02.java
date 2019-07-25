/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode x = new ListNode(0);
        ListNode y = x;
        int cry = 0;
        while(true){
            if((l1==null)&&(l2==null)) break;
            if(l1!=null){
                if(l2!=null){
                    x.next = new ListNode(l1.val + l2.val + cry);
                    l2 = l2.next;
                }
                else x.next = new ListNode(l1.val + cry);
                l1 = l1.next;
                
            }
            else if((l1==null)&&(l2!=null)){
                x.next = new ListNode(l2.val + cry);
                l2 = l2.next;
            }
            x = x.next;
            if(x.val>=10){
                cry = 1;
                x.val = x.val%10;
            }
            else cry = 0;
            }
        if(cry==1)  x.next = new ListNode(cry);
        return y.next;
    }
}
