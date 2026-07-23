from pyspark import pipelines as dp

@dp.table(
    name = "customer_info"
)
def get_data():
  return spark.readStream.table("dlt_cat.dlt_sch.customer_info")