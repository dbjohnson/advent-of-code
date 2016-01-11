(def key "ckczppom")

(defn md5
  ; http://rosettacode.org/wiki/MD5#Clojure
  [input]
  (apply str
    (map (partial format "%02x")
      (.digest (doto (java.security.MessageDigest/getInstance "MD5")
                     .reset
                     (.update (.getBytes input)))))))

(defn hashit
  [d]
  (md5 (format "%s%s" key (str d))))

(defn winner?
  [d num-zeros]
  (every? #{\0} (take num-zeros (hashit d))))

(defn find-first-with-n-zeros 
  [num-zeros]
  (loop [i 0]
    (if (winner? i num-zeros)
      i
      (recur (inc i)))))

(println "part 1:" (find-first-with-n-zeros 5))
(println "part 2:" (find-first-with-n-zeros 6))
