val input = scala.io.Source.fromFile("input.txt").getLines.map(_.split("x").map(_.toInt)).toList

def dimsToSides(dims: Array[Int]) = {
    // A shame - can't use combinations, because it returns the set of unique
    // combinations, which would potentially discard one or more sides
    // val sides = dims.combinations(2).toList
    val Array(l, w, h) = dims
    List(List(l, w), List(w, h), List(h, l))
}

def paperRequired(dims: Array[Int]) = {
    val sides = dimsToSides(dims)
    val side_areas = sides.map(_.product) 
    val smallest_side = side_areas.min 
    val total_area = side_areas.sum * 2
    total_area + smallest_side 
}

def ribbonRequired(dims: Array[Int]) = {
    val volume = dims.product 
    val sides = dimsToSides(dims)
    val perimeters = sides.map(_.sum * 2)
    volume + perimeters.min
}

println(s"part 1: ${input.map(box => paperRequired(box)).sum}")
println(s"part 2: ${input.map(box => ribbonRequired(box)).sum}")
