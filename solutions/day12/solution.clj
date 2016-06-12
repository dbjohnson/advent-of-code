(require '[clojure.data.json :as json])

(defn seqsum 
  "Returns the sum of all numbers in a sequence"
  [s] 
  {:test (defn f [] (assert (= 6 (seqsum [1 2 "a" 3]))))}
  (let [numbers (filter number? s)
        seqs (filter sequential? s)
        maps (filter map? s)
        numsum (reduce + numbers)
        ssum (reduce + (map seqsum seqs))
        msum (reduce + (map mapsum maps))]
    (+ numsum ssum msum)))

(defn mapsum
  "Returns the sum of all numbers in a map's keys and values"
  [m]
  {:test (defn f[] (assert (= (6 mapsum {1 2 2 1}))))}
  (+ (seqsum (keys m))
     (seqsum (vals m))))

(defn filter-by-val
  "Recursively removes any branches in a map whose values contain the specified string" 
  [v m]
  {:test (defn f[] (assert (= {1 2 3 nil} (filter-by-val {1 2 3 {4 "red"}}))))}
  (cond
    (sequential? m) (map #(filter-by-val v %) m)
    (map? m)
      (when (not (some #{v} (vals m)))
        (into {}
           (map
             (fn [[k, vv]]
               [k, (filter-by-val v vv)])
             m)))
    :else m))

(def input (json/read-str (slurp "input.txt")))
(println "part 1: " (mapsum input))
(println "part 2: " (mapsum (filter-by-val "red" input)))
