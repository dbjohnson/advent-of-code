(def input (->> (slurp "input.txt")
                (clojure.string/split-lines)
                (map #(clojure.string/split % #"x"))
                (map #(map read-string %))))

(defn dims->sides
  [[l w h]]
  [[l w] [w h] [h l]])

(defn paper-required 
  [dims]
  (let [sides (dims->sides dims) 
        side-areas (map #(reduce * %) sides)
        total-area (reduce + (map #(* 2 %) side-areas))
        extra (apply min side-areas)]
    (+ total-area extra)))

(defn volume 
  [dims]
  (reduce * dims))

(defn shortest-perimeter
  [dims]
  (let [sides (dims->sides dims)
        perimeters (map #(* 2 (reduce + %)) sides)]
    (apply min perimeters)))

(defn ribbon-required
  [dims]
  (+ (volume dims) (shortest-perimeter dims)))

(defn part1 
  [input]
  (reduce + (map paper-required input)))

(defn part2 
  [input]
  (reduce + (map ribbon-required input)))

(println "part 1:" (part1 input))
(println "part 2" (part2 input))
