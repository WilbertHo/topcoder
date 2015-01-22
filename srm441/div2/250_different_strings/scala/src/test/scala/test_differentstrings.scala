import org.scalatest._

class DifferentStringsSpecs extends FlatSpec with Matchers {
  it should "koder vs topcoder" in {
    val df = new DifferentStrings("koder", "topcoder")
    val diff = df.minimize
    diff should be (1)
  }
  it should "hello vs xello" in {
    val df = new DifferentStrings("hello", "xello")
    val diff = df.minimize
    diff should be (1)
  }
  it should "abc vs topabcoder" in {
    val df = new DifferentStrings("abc", "topabcoder")
    val diff = df.minimize
    diff should be (0)
  }
  it should "adaabc vs aababbc" in {
    val df = new DifferentStrings("adaabc", "aababbc")
    val diff = df.minimize
    diff should be (2)
  }
  it should "giorgi vs igroig" in {
    val df = new DifferentStrings("giorgi", "igroig")
    val diff = df.minimize
    diff should be (6)
  }
}
