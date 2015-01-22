import org.scalatest._

class TheConsecutiveIntegersDivTwoSpecs extends FlatSpec with Matchers {
  it should "4, 47, 7" in {
    val ci = new TheConsecutiveIntegersDivTwoSpecs
    val m = ci((4, 47, 7), 2)
    m should be (2)
  }
}
