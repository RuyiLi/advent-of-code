object BinaryBoarding {
	def main(args: Array[String]): Unit = {
		val rows = io.Source.stdin.getLines.toList
		println(partOne(rows))
		println(partTwo(rows))
	}

	def getSeatID(seat: String): Int = {
		def parseInstr (bounds: (Int, Int), instr: Char): (Int, Int) = {
			val mid = (bounds._1 + bounds._2).toFloat / 2
			if (instr == 'F' || instr == 'L') (bounds._1, Math.floor(mid).toInt) 
			else (Math.ceil(mid).toInt, bounds._2)
		}
	
		val row = seat.take(7).foldLeft((0, 127))(parseInstr)._1
		val col = seat.takeRight(3).foldLeft((0, 7))(parseInstr)._1
		row * 8 + col
	}

	def partOne(rows: List[String]): Int = (rows map getSeatID).max

	def partTwo(rows: List[String]): Int = {
		val seats = (rows map getSeatID)
						.sorted
						.zipWithIndex
		
		// requires rows.length > 2
		def findUnique(seats: List[(Int, Int)], last: Int): Int = 
			(seats.head._2 - seats.head._1) match {
				case `last` => findUnique(seats.tail, last)
				case _ => seats.head._1 - 1
			}
		
		findUnique(seats.tail, seats.head._2 - seats.head._1)
	}
}
