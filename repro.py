import sys

print(sys.path)
import google
print(google)
from google.cloud import bigquery
from google.cloud import storage

def main():
  print("You'll never see me :(")

if __name__ == '__main__':
  main()
