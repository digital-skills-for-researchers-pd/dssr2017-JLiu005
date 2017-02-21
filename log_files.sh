#!/bin/bash

DIR="data_output"
mkdir -p $DIR

x=$(find ~/Desktop/pipeline_manager/data_input -name '*.txt' | wc -l)
if [ $x -eq 0 ]
then
	echo "No files found"
else	
	echo "Files found, recorded in LOG.txt"
	find ~/Desktop/pipeline_manager/data_input -name '*.txt' -print >> $DIR/log.txt

fi


