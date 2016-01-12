(defn cartesian-product
  [xmin xmax ymin ymax]
  (for [x (range xmin xmax)
        y (range ymin ymax)]
    [x y]))


(defn parse-instruction
  [instruction]
  (let [pattern #"(toggle|turn off|turn on) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)"
        matches (re-matches pattern instruction)
        xs (map read-string (map #(nth matches %) [2 4]))
        ys (map read-string (map #(nth matches %) [3 5]))
        [xmin xmax] (sort xs)
        [ymin ymax] (sort ys)]
        {:action (nth matches 1)
         :indexes (cartesian-product xmin (inc xmax) ymin (inc ymax))})) 

(def instructions (->> (slurp "input.txt")
                       (clojure.string/split-lines)
                       (map parse-instruction)))

(defn process-instruction
  [instruction lights action->fn]
  (let [fn (action->fn (:action instruction))]
    (loop [[idx & more] (:indexes instruction)
           lights lights]
      (if idx 
        (let [[x y] idx
              loc {:x x :y y}
              curr-val (or (lights loc) 0)
              next-val (fn curr-val)]
            (recur more 
                   (assoc lights loc next-val)))
        lights))))

(defn solve
  [instructions action->fn]
  (loop [[instruction & more] instructions
         lights {}]
    (if instruction
      (recur more
             (process-instruction instruction lights action->fn))
      lights)))

(defn part1
  [instructions]
  (let [action->fn {"toggle" #(if (zero? %) 1 0) 
                    "turn on" (constantly 1)
                    "turn off" (constantly 0)}]
    (reduce + (vals (solve instructions action->fn)))))

(defn part2
  [instructions]
  (let [action->fn {"toggle" #(+ % 2) 
                    "turn on" #(+ % 1)
                    "turn off" #(max 0 (- % 1))}]
    (reduce + (vals (solve instructions action->fn)))))

(println "part 1:" (part1 instructions))
(println "part 2:" (part2 instructions))
