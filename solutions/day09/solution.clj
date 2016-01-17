(use '[leiningen.exec :only (deps)])
(deps '[[org.clojure/data.priority-map "0.0.7"]]
      :repositories {"priority-map" "https://github.com/clojure/data.priority-map"})
(require '[clojure.data.priority-map :as pm])
(require '[clojure.string :as str])

(defn line->city-pair
  [string]
  (let [[cities dist] (str/split string #" = ")
        dist (read-string dist)
        [c1 c2] (str/split cities #" to ")]
    {{c1 c2} dist {c2 c1} dist}))

(def distance-map (->> (slurp "input.txt")
                       (str/split-lines)
                       (map line->city-pair)
                       (reduce conj)))

(def cities (->> (keys distance-map)
                 (map seq)
                 (flatten)
                 (set)))

(defn path->cost-so-far
  [path distance-map]
  (->> (map hash-map path (next path))
       (map distance-map)
       (reduce +)))

(defn path->heuristic
  [path distance-map cities]
  (let [min-dist (apply min (vals distance-map))]
    (* min-dist (- (count cities) (count path)))))

(defn path->cost
  [path distance-map cities]
  (+ (path->cost-so-far path distance-map)
     (path->heuristic path distance-map cities)))
    
(defn path->children
  [path distance-map cities]
  (->> cities 
       (filter (complement (set path))) ; remove any cities that are already on the path
       (map #(conj path %))
       ; put cost alongside path for easy use with priority-map conj
       (map #(vector % (path->cost % distance-map cities))) 
       (reduce concat)))

(defn A* 
  [distance-map cities]
  (loop [q (apply pm/priority-map (path->children [] distance-map cities))
         best-cost nil]
    (if-let [[path cost] (peek q)]
      (if (and best-cost (< best-cost cost))
        ; if the best path available on the q costs more than the best solution we've found so far, we're done 
        best-cost 
        (let [children (path->children path distance-map cities)
              q (pop q)]
          (if (empty? children)
            (recur q cost) ; complete path - if we've gotten here, it's also the lowest-cost complete path
            (recur (apply assoc q children) best-cost)))))))

(defn part1
  [distance-map cities]
  (A* distance-map cities))

(defn part2
  [distance-map cities]
  ; invert the city-to-city distance map, effectively making A* maximize the cost
  (let [neg-distances (map #(* -1 %) (vals distance-map))
        neg-distance-map (zipmap (keys distance-map) neg-distances) ]
    (* -1 (A* neg-distance-map cities))))

(println "part 1:" (part1 distance-map cities))
(println "part 2:" (part2 distance-map cities))
