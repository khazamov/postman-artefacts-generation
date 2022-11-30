rm -f api-postman-specifications/* && mkdir api-postman-specifications

for file in api-specifications/*
do
  openapi2postmanv2 -s "$file" -o api-postman-specifications/"$(basename -- $file)" -p -O folderStrategy=Tags,requestParametersResolution=Schema,responseParametersResolution=Schema,optimizeConversion=false,stackLimit=50
done
