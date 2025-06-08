class Solution {
    public static void lexical(int n,int num,List<Integer> nums)
    {
        if(num>n)
        return;
        else{
            nums.add(num);
            for(int i=0;i<10;i++)
            {
                if(num*10+i>n)
                    return;
                lexical(n,num*10+i,nums);
            }
        }
    }
    public List<Integer> lexicalOrder(int n) {
        List<Integer> nums=new ArrayList<>();
        for(int i=1;i<10;i++)
            lexical(n,i,nums);
        return nums;
    }
    
}