class DifferentStrings(shorter: String, longer:String) {
  def minimize: Int = {
    ((0 to longer.length - shorter.length).map( i =>
      shorter zip longer.slice(i, i + shorter.length) count {
        pair => pair._1 != pair._2
      }
    )).toList.min
  }
}
