(def moves (->> (slurp "input.txt")
                (map #(if (= \( %) 1 -1)))) 

(defn cumsum
  [s]
  (reduce
    (fn [cs x] 
      (conj cs (+ (or (last cs) 0) x)))
    []
    s))

(println "part 1:" (reduce + moves))
(println "part 2:" (inc (.indexOf (cumsum moves) -1)))
