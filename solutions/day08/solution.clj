(require '[clojure.string :as str])

(def input (str/split-lines (slurp "input.txt")))

(defn encoding-overhead 
  [string]
  (+ (* 3 (count (re-seq #"\\x[0-9a-f]{2}" string)))
     (count (re-seq #"\\[\\|\"]" string))
     2))

(defn overhead-to-encode 
  [string]
  (+ (count (re-seq #"[\"|\\]" string)) 
     2)) 

(defn part1
  [input]
  (reduce + (map encoding-overhead input)))

(defn part2
  [input]
  (reduce + (map overhead-to-encode input)))

(println "part 1:" (part1 input))
(println "part 2:" (part2 input))
