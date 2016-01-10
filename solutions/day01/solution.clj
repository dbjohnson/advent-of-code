(def moves (->> (slurp "input.txt")
                (map #(if (= \( %) 1 -1)))) 

(defn part1 
  [moves]
  (reduce + moves))

(defn part2 
  [moves]
  (loop [[move & moves] moves
         floor 0
         step 0]
    (if (= -1 floor) 
      step
      (recur moves
             (+ floor move)
             (inc step))))) 

(println "part 1" (part1 moves))
(println "part 2:" (part2 moves))
