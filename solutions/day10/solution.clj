(defn look-and-say
  [string]
  (->> string
       (re-seq #"([0-9])\1*")
       (map first)
       (map #(str (count %) (first %)))
       (apply str)))

(println "part 1:" (count (nth (iterate look-and-say "1113122113") 40)))
(println "part 2:" (count (nth (iterate look-and-say "1113122113") 50)))
