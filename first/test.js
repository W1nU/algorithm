function solution(A) {
   let min_num = Math.min(...A)
   let max_num = Math.max(...A)
   let count = 0
   
   while(min_num<max_num){
      if(max_num-min_num===1){
         for(let num of A){
            if(num>min_num){
               num--
               count++
            }
         }
         break;
      }else{
         next_max = max_num - 1
         next_min = min_num + 1
         
         for(let num of A){
            if(num>next_max){
               num--
               count++
            }else if(num<next_min){
               num ++
               count ++
            }
         }

         min_num = next_min
         max_num = next_max
      }
   }
   return count
}

console.log(solution([1, 10, 1, 10]))

 