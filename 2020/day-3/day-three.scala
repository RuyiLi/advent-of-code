object TobogganTrajectory {
	def main(args: Array[String]): Unit = {
		val rows = io.Source.stdin.getLines.toList.tail
		println(partOne(rows))
		println(partTwo(rows))	
	}

	def encounters(rows: List[String], dx: Int, dy: Int, x: Int = 0, y: Int = 1): Long = {
		if (rows.length == 0) 
			return 0

		if (y % dy > 0)
			return encounters(rows.tail, dx, dy, x, y + 1)
		
		val head = rows.head
		val hasTreeVal = if (head.charAt((x + dx) % head.length) == '#') 1 else 0
		return hasTreeVal + encounters(rows.tail, dx, dy, x + dx, y + 1)
	}

	def partOne(rows: List[String]): Long
		= encounters(rows, 3, 1)

	def partTwo(rows: List[String]): Long 
		= encounters(rows, 1, 1) * 
			encounters(rows, 3, 1) * 
			encounters(rows, 5, 1) * 
			encounters(rows, 7, 1) * 
			encounters(rows, 1, 2)
}
