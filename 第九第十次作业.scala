import scala.collection.mutable.ListBuffer

/**
  * Created by 旭宝 on 2018/7/20.
  */
 /*object hscala1 {
    def main(args:Array[String]){
      var miao=List(20,25,30,35,40,25)
      var b=4
      for (i<-Range(0,5)){
        if(i == 2){
          println("周三"+"温度："+miao(i))
        }else{
          println(miao(i))
        }
      }
    }
  }


  object test2{
    def main(args: Array[String]) {
      1.to(10).map(i=>i*10).foreach(i=>println(i))
    }
  }




  }

*/


object YaSpark{
  def main(args: Array[String]){
    import org.json.JSONObject
    import org.apache.spark.SparkConf
    import org.apache.spark.SparkContext

    val conf = new SparkConf().setAppName("cala").setMaster("local")
    val sc=new SparkContext(conf)


    sc.textFile("E:\\hyy-o\\src\\main\\scala\\全国招生人数.txt")
      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{
        val json = new JSONObject(line)
          val jsonlist=json.getJSONArray("data")
        val list=ListBuffer[JSONObject]()
        for(i<-0 to  jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })

      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))
  }
}


