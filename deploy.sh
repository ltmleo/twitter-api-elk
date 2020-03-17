#!/bin/bash
set -e
#baixar helm
#minikube start (verificar)
#helm init

if test -z $1 ; then
  echo "Missing Password"
  exit 1
fi

helm delete --purge save-tweets || echo "Installing it now"
helm upgrade --install save-tweets ./infra/application/ -f ./save-tweets/env/values.yaml --set password="$1"