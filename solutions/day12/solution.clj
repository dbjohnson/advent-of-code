(require '[clojure.data.json :as json])

(defn json-sum
  "Returns the sum of all numbers in a json object"
  {:test (defn f[] (assert (= (10 json-sum [1 2 {3 4}]))))}
  [j]
  (cond
    (map? j)
      (reduce + (map json-sum [(keys j) (vals j)]))
    (sequential? j)
      (reduce + (map json-sum j))
    :else
      (if (number? j) j 0)))

(defn filter-json-by-val
  "Recursively filters any json serialized object - which can be any arbitrary 
   nested combination of lists, maps, and literals - removing any maps that 
   contain the specified value"
  [v j]
  {:test (defn f[] (assert (= {1 2 3 nil} (filter-json-by-val {1 2 3 {4 "red"}}))))}
  (cond
    (map? j)
      (when (not (some #{v} (vals j)))
        (into {}
           (map
             (fn [[k, vv]]
               [k, (filter-json-by-val v vv)])
             j)))
    (sequential? j) 
      (map #(filter-json-by-val v %) j)
    :else 
      j))

(def input (json/read-str (slurp "input.txt")))
(println "part 1: " (json-sum input))
(println "part 2: " (json-sum (filter-json-by-val "red" input)))
