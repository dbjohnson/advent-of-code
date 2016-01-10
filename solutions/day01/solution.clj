(defn move-to-offset [move]
  (if (= move \() 1 -1))

(def moves (map move-to-offset (seq (slurp "input.txt"))))

(defn part1 [moves]
  (println "part 1:" (reduce + moves)))

(defn part2 [moves]
  (loop [[move & moves] moves
         pos 0
         step 0]
    (if (= -1 pos) 
       (println "part 2:" step)
       (recur moves
              (+ pos move)
              (inc step))))) 

(part1 moves)
(part2 moves)
