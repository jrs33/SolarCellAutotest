#!/usr/bin/python3
import boto3
import csv

BUCKET_NAME = 'solarbytes-csv-uploads'
KEY_NAME = 'solarbytes.csv'
BUFFER_FILE = '/home/pi/Desktop/solarbytes.csv'

try:
	s3 = boto3.client('s3')

	with open(BUFFER_FILE,"rb") as csvfileObject:
		s3.upload_fileobj(csvfileObject, BUCKET_NAME, KEY_NAME)

	print('[INFO]	buffer file successfully uploaded to s3 bucket')
except Exception as e:
	print(e)
