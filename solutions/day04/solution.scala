val key = "ckczppom"

def md5(s: String) = {
    val d = java.security.MessageDigest.getInstance("MD5").digest(s.map(_.toByte).toArray)
    d.map(b => f"$b%02x").mkString("")
}

def findFirstWithNzeros(n: Int) : Int = {
    var i = 0
    while(i < Int.MaxValue) {
        val d = md5(key + i.toString)
        if (d.startsWith("0" * n)) {
            return i
        }
        i += 1
    }
    throw new IllegalStateException("Didn't find it!")
}

for ((part, zeros) <- List(("part 1", 5), ("part 2", 6))) {
    println(s"${part}: ${findFirstWithNzeros(zeros)}")
}
