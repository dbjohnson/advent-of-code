(require '[clojure.string :as str])

(def cmd->fn {"OR" #(bit-or %1 %2)
              "AND" #(bit-and %1 %2)
              "RSHIFT" #(bit-shift-right %1 %2)
              "LSHIFT" #(bit-shift-left %1 %2)
              "NOT" #(bit-not %)
              "SET" #(identity %)})

(defn make-input
  [x]
  (fn [circuit]
    (if (re-find #"^[0-9]+$" x)
      (read-string x)
      (circuit x))))

(defn instruction->switch 
  [instruction]
  (let [[input target] (str/split instruction #" -> ")
        parts (str/split input #" ")
        commands (set (keys cmd->fn))
        cmd (or (first (filter commands parts)) "SET")
        operands (map make-input (remove commands parts))]
    {:fn (cmd->fn cmd)
     :operands operands
     :target target
     :inputs (fn [circuit] (map #(% circuit) operands))}))

(def switches (->> (slurp "input.txt")
                   (str/split-lines)
                   (map instruction->switch)))

(defn switches->circuit 
  ([switches] (switches->circuit switches {}))
  ([switches init-circuit]
    (loop [[switch & more] switches
           circuit init-circuit]
      (if switch
        (if (circuit (:target switch))
          (recur more circuit)
          (let [inputs ((:inputs switch) circuit)]
            (if (every? (complement nil?) inputs)
              (recur more (assoc circuit (:target switch) (apply (:fn switch) inputs)))
              (recur (conj (vec more) switch) circuit))))
        circuit))))

(defn part1
  [switches]
  ((switches->circuit switches) "a"))

(defn part2
  [switches init-circuit]
  ((switches->circuit switches init-circuit) "a"))

(println "part 1:" (part1 switches))
(println "part 2:" (part2 switches {"b" (part1 switches)}))
