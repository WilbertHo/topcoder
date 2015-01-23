class TheConsecutiveIntegersDivTwo {
  def find(numbers: Seq[Int], k: Int): Int = {
    if (k < 2)
      0
    else
      numbers.sorted.sliding(k).map( pair => pair(1) - pair(0)).min - 1
  }
}
