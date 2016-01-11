(defn parse-instruction
  [instruction]
  (let [pattern #"(toggle|turn off|turn on) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)"
        matches (re-matches pattern instruction)
        xs (map read-string (map #(nth matches %) [2 4]))
        ys (map read-string (map #(nth matches %) [3 5]))]
        {:action (nth matches 1)
         :x_from (apply min xs)
         :y_from (apply min ys)
         :x_to (apply max xs)
         :y_to (apply max ys)})) 

(def instructions (->> (slurp "input.txt")
                       (clojure.string/split-lines)
                       (map parse-instruction)))

(defn process-instruction
  [instruction lights fnmap]
  (let [action (fnmap (:action instruction))
        idxs (for [x (range (:x_from instruction) (inc (:x_to instruction)))
                   y (range (:y_from instruction) (inc (:y_to instruction)))]
               [x y])]
    (loop [[idx & more] idxs
           lights lights]
      (if idx 
        (let [[x y] idx
              loc {:x x :y y}
              curr-val (or (lights loc) 0)
              next-val (action curr-val)]
            (recur more 
                   (assoc lights loc next-val)))
        lights))))

(defn solve
  [instructions fnmap]
  (loop [[instruction & more] instructions
         lights {}]
    (if instruction
      (recur more
             (process-instruction instruction lights fnmap))
      lights)))

(defn part1
  [instructions]
  (let [fnmap {"toggle" #(if (zero? %) 1 0) 
               "turn on" (constantly 1)
               "turn off" (constantly 0)}]
    (reduce + (vals (solve instructions fnmap)))))

(defn part2
  [instructions]
  (let [fnmap {"toggle" #(+ % 2) 
               "turn on" #(+ % 1)
               "turn off" #(max 0 (- % 1))}]
    (reduce + (vals (solve instructions fnmap)))))

(println "part 1:" (part1 instructions))
(println "part 2:" (part2 instructions))
