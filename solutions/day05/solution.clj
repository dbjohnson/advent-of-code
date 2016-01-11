(def words (->> (slurp "input.txt")
                (clojure.string/split-lines)))

(defn vowel-count
  [word]
  (let [vowels (set "aeiou")]
    (count (filter vowels word))))

(defn has-double
  [word]
  (not (nil? (re-matches #".*(([a-z])\2{1}).*" word))))

(defn has-bad
  ([word] (has-bad word ["ab" "cd" "pq" "xy"]))
  ([word bad]
    (->> (map #(re-pattern (format ".*%s.*" %)) bad)
         (map #(re-matches % word))
         (every? nil?)
          not)))

(defn nice?
  [word]
  (every? true? [(< 2 (vowel-count word))
                 (has-double word)
                 (not (has-bad word))]))

(defn has-repeat-pair
  [word]
  (not (nil? (re-matches #".*([a-z]{2}).*\1.*" word))))

(defn has-repeat-letter
  [word]
  (not (nil? (re-matches #".*([a-z])[a-z]\1.*" word))))

(defn nicer?
  [word]
  (and (has-repeat-pair word) (has-repeat-letter word)))

(println "part 1:" (count (filter nice? words)))
(println "part 2" (count (filter nicer? words)))
