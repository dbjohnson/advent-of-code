(def steps (seq (slurp "input.txt")))

(defn move
  [pos step]
  (let [coord (if (#{\>, \<} step) :x :y)
        step (if (#{\>, \^} step) 1 -1)]
    (assoc pos coord (+ (coord pos) step))))

(defn route
  [steps]
  (loop [[step & more] steps
         pos {:x 0 :y 0}
         route []]
    (let [route (conj route pos)]
      (if step
        (recur more 
               (move pos step) 
               (conj route pos))
        route))))

(defn num-distinct
  [route]
  (count (set route)))

(defn part1
  [steps]
  (num-distinct (route steps)))

(defn part2
  [steps]
  (let [santa (route (take-nth 2 steps))
        robo-santa (route (take-nth 2 (rest steps)))]
    (num-distinct (concat santa robo-santa))))

(println "part 1:" (part1 steps))
(println "part 2:" (part2 steps))
