#!/bin/bash
#POST request to the passed URL using curl, and display the body of the response
curl -s -X POST -d "subject=I will always be here for PLD&email=test@gmail.com" "$1"
