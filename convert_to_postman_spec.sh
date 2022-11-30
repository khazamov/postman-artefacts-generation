for file in api-specifications/*
do
  openapi2postmanv2 -s "$file" -o "$(basename -- $file)" -p -O folderStrategy=Tags,requestParametersResolution=Schema,responseParametersResolution=Schema,optimizeConversion=false,stackLimit=50
done
