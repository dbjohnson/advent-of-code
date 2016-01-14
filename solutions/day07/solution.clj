(require '[clojure.string :as str])

(def cmd->fn {"OR" #(bit-or %1 %2)
              "AND" #(bit-and %1 %2)
              "RSHIFT" #(bit-shift-right %1 %2)
              "LSHIFT" #(bit-shift-left %1 %2)
              "NOT" #(bit-not %)
              "SET" #(identity %)})

(defn make-wire
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
        operands (map make-wire (remove commands parts))]
    {:inputs (fn [circuit] (map #(% circuit) operands))
     :fn (cmd->fn cmd)
     :target target}))

(def switches (->> (slurp "input.txt")
                   (str/split-lines)
                   (map instruction->switch)))

(defn switches->circuit 
  ([switches] (switches->circuit switches {}))
  ([switches init-circuit]
    (loop [[switch & more] switches
           circuit init-circuit]
      (if switch
        (let [inputs ((:inputs switch) circuit)]
          (if (not-any? nil? inputs)
            (recur more (assoc circuit (:target switch) (apply (:fn switch) inputs)))
            ; inputs for this switch aren't set, so put it at the end of the list 
            (recur (conj (vec more) switch) circuit)))
        circuit))))

(defn part1
  [switches]
  ((switches->circuit switches) "a"))

(defn part2
  [switches init-circuit]
  (let [set-switches (set (keys init-circuit))
        switches (filter #(not (set-switches (:target %))) switches)]
    ((switches->circuit switches init-circuit) "a")))

(println "part 1:" (part1 switches))
(println "part 2:" (part2 switches {"b" (part1 switches)}))
