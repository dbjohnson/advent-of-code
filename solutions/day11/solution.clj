(def alphabet "abcdefghijklmnopqrstuvwxyz")

(defn str->idxs
  "Convert a string to a sequence of integer indices"
  {:test (fn [] (assert (= [0 1 2] (str->idxs "abc"))))}
  [string]
  (map #(.indexOf alphabet (str %)) string))
  
(defn idxs->str 
  "Convert a sequence of integer indices to string"
  {:test (fn [] (assert (= "abc" (idxs->str [0 1 2]))))}
  [idxs]
  (apply str (map #(nth alphabet %) idxs)))
  
(defn seq->n-tuples
  "Transforms a sequence to a sequence of n-tuples where each n-tuple
  corresponds to the element at the same position in the original sequence
  followed by the (n-1) subsequent values"
  {:test (fn [] (assert (= [[0 1 2] [1 2 3] [2 3 4]] 
                           (seq->n-tuples 3 [0 1 2 3 4]))))}
  [n s]
  (->> (iterate next s)
       (take n)
       (apply map vector)))

(defn seq->diffs
  "Calculates the differences between consecutive elements in a sequence"
  {:test (fn [] (assert (= [1 2 -1] (seq->diffs [1 2 4 3]))))}
  [s]
  (->> (seq->n-tuples 2 s) 
       (map reverse)
       (map #(apply - %))))

(defn has-straight?
  "Determines whether a string has a run of characters of length run-length 
  where each character in the run is one higher than the last"
  [string run-length]
  (->> (str->idxs string)
       (seq->diffs)
       (seq->n-tuples (dec run-length))
       (some #(= (set %) #{1}))))

(defn contains-forbidden?
  "Check string for disallowed characters"
  [string forbidden]
  (some #(.contains string (str %)) forbidden))

(defn unique-pair-count
  "Calculate the number of unique adjacent pairs of identical characters within a string"
  [string]
  (->> string
       (re-seq #"([\w])\1{1}")
       (map first)
       set
       count))

(defn inc-str
  "Increment string by one character"
  {:test (fn [] (assert (= (inc-str "aa") "ab"))
                (assert (= (inc-str "bz") "ca")))}
  [string]
  (let [idxs (str->idxs string)
        idx-limit (dec (count alphabet))]
    (loop [incd-idxs (apply vector idxs)
           pos (dec (count idxs))]
      (if (> 0 pos)
        string
        (if (= (nth incd-idxs pos) idx-limit)
          (recur (assoc incd-idxs pos 0) (dec pos))
          (let [incd (assoc incd-idxs pos (inc (nth incd-idxs pos)))]
            (idxs->str incd)))))))

(defn valid-password?
  "Test validity of a candidate password"
  [pwd n-uniq-pairs straight-len forbidden]
  (and (not (contains-forbidden? pwd forbidden))
       (<= n-uniq-pairs (unique-pair-count pwd))
       (has-straight? pwd straight-len)))

(defn next-password
  "Find the next valid password after the provided value"
  ([pwd] (next-password pwd 2 3 "iol"))
  ([pwd n-uniq-pairs straight-len forbidden]
    (loop [pwd (inc-str pwd)]
      (if (valid-password? pwd n-uniq-pairs straight-len forbidden)
        pwd
        (recur (inc-str pwd))))))

(def nxt (next-password "vzbxkghb"))
(println "part 1: " nxt)
(println "part 2: " (next-password nxt))
