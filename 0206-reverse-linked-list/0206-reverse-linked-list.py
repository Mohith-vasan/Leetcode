class Solution(object):
    def reverseList(self, head):
        st=[]
        temp=head
        while temp!=None:
            st.append(temp.val)
            temp=temp.next
        temp=head
        while temp!=None:
            temp.val=st.pop()
            temp=temp.next
        return head #this is output