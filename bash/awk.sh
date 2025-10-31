#!/bin/bash
awk -F',' '{print $1, $3}' data/Sales_raw.csv