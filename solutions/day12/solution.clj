(require '[clojure.data.json :as json])
(def input (json/read-str (slurp "input.txt")))

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
  [m]
  (+ (seqsum (keys m))
     (seqsum (vals m))))

(defn filter-by-val
  [v m]
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

(println "part 1: " (mapsum input))
(println "part 2: " (mapsum (filter-by-val "red" input)))
