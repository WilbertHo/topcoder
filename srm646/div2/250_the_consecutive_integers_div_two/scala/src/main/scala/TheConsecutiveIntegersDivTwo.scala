class TheConsecutiveIntegersDivTwo {
  def find(numbers: Array[Int], k: Int): Int = {
    numbers.productIterator.map(x => x.asInstanceOf[Int]).toList.sorted.sliding(2).map( pair => pair(1) - pair(0)).min
  }
}
