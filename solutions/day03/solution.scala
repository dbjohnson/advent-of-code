val path = scala.io.Source.fromFile("input.txt").toList

val coord = Map('>' -> 'x',
                '<' -> 'x',
                '^' -> 'y',
                'v' -> 'y')

val dir = Map('>' -> 1,
              '<' -> -1,
              '^' -> 1,
              'v' -> -1)

def locationsVisited(steps: List[Char]) = {
    val pos = collection.mutable.Map('x' -> 0,
                                     'y' -> 0)
    val visited = collection.mutable.Set[Any]()
    for (step <- steps) {
        pos(coord(step)) += dir(step) 
        visited += pos.clone()
    }
    visited
}

val visited = locationsVisited(path)
println(s"part 1: ${visited.size}")

val grouped = path.grouped(2).toList
val santaSteps = grouped.map(_(0))
val robotSteps = grouped.map(_(1))
val allVisited = locationsVisited(santaSteps) | locationsVisited(robotSteps)
println(s"part 2: ${allVisited.size}")
