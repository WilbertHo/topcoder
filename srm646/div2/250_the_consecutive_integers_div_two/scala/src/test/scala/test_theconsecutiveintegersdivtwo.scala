import org.scalatest._

class TheConsecutiveIntegersDivTwoSpecs extends FlatSpec with Matchers {
  it should "4, 47, 7" in {
    val ci = new TheConsecutiveIntegersDivTwo
    val m = ci.find(List(4, 47, 7), 2)
    m should be (2)
  }
  it should "1, 100" in {
    val ci = new TheConsecutiveIntegersDivTwo
    val m = ci.find(List(1, 100), 1)
    m should be (0)
  }
  it should "-96, -53, 82, -24, 6, -75" in {
    val ci = new TheConsecutiveIntegersDivTwo
    val m = ci.find(List(-96, -53, 82, -24, 6, -75), 2)
    m should be (20)
  }
}
