if I store the prefix sum of the # of vowels before index i and calculate the sum of all vowels in each sub string I will generally use the ff formula where a sub string sub whose start index is s and end index is e
`#vowels = Σpresum[e] - presum[s] where e  0 <= e < s < len(word)`
and we are guaranteed that presum is sequence of  numbers 0,1,2,3,,,,,,
therefore if we let ai be frequency of i in presum
and xi be # of  total vowels created by all substrings upto index i
` xi= Σ(i-j)*ai*aj` for j ={0,,i}
our final answer = Σxi` for i ={0,,total vowels in word}