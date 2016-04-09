(def alphabet "abcdefghijklmnopqrstuvwxyz")

(defn str->idxs
  [string]
  (map #(.indexOf alphabet (str %)) string))
  
(defn idxs->str 
  [idxs]
  (apply str (map #(nth alphabet %) idxs)))
  
(defn has-straight?
  [string run-length]
  (let [idxs (str->idxs string)
        diffs (map #(apply - %) (map vector (next idxs) idxs))
        n-tuples (apply map vector (take (dec run-length) (iterate next diffs)))
        is-run (map (fn [n-tuple] (every? #(= 1 %) n-tuple)) n-tuples)]
    (some identity is-run)))

(defn contains-forbidden?
  [string & forbidden]
  (some #(.contains string %) forbidden))

(defn pair-count
  [string]
  (count (re-seq #"([\w])\1{1}" string)))

(defn inc-str
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
  [pwd]
  (and (not (contains-forbidden? pwd "i" "o" "l"))
       (< 1 (pair-count pwd))
       (has-straight? pwd 3)))

(defn next-password
  [password]
  (loop [pwd (inc-str password)]
    (if (valid-password? pwd)
      pwd
      (recur (inc-str pwd)))))

(def nxt (next-password "vzbxkghb"))
(println "part 1: " nxt)
(println "part 2: " (next-password nxt))
