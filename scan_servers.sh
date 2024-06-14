#!/bin/bash

# TSUNAMI_JAR=tsunami-main-0.0.23-SNAPSHOT-cli.jar
TARGET_FILE=targets.txt
RESULTS_DIR=results

mkdir -p $RESULTS_DIR

while IFS= read -r target; do
  echo "Scanning $target"
  java \
    -cp "tsunami.jar:plugins/*" \
    -Dtsunami-config.location=tsunami.yaml \
    com.google.tsunami.main.cli.TsunamiCli \
    --ip-v4-target=$target \
    --scan-results-local-output-format=JSON \
    --scan-results-local-output-filename=$RESULTS_DIR/tsunami-output-$target.json
done < "$TARGET_FILE"
