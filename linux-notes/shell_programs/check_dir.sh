#! /bin/bash
if [ -d "test" ]	# the space in [] must exists; -f check the if the file exists
then
  echo "directory test has already exists."
else
  mkdir test
fi