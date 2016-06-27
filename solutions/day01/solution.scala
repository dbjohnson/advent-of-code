val input = scala.io.Source.fromFile("input.txt").toList.map(x => if (x == '(') 1 else -1)
println(s"part 1: ${input.sum}")

val cumsum = input.map{var s = 0; d => {s += d; s}}
println(s"part 2: ${cumsum.indexOf(-1) + 1}")
