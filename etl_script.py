import pandas as pd
import boto3


s3 = boto3.client('s3')
bucket_name ="yhonathann.mytestbucket"
file_ley = "IngresantesPrograma_2112025_174553.csv"

obj=s3.get_object(Bucket=bucket_name,Key=file_ley)

df = pd.read_csv(obj['body'])


df_clean = df.dropna()

output_key = "datos_limpios.csv"

s3.put_object(Bucket= bucket_name,Key=output_key,Body= df_clean.to_csv(index=False))

print("Proceso ETL completado")
