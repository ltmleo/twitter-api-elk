#!/bin/bash
set -e
#baixar helm
#minikube start (verificar)
#helm init

# if test -z $1 ; then
#   echo "Missing Password"
#   exit 1
# fi

#helm delete --purge save-tweets || echo "Installing it now"
#helm upgrade --install save-tweets ./infra/application/ -f ./save-tweets/env/values.yaml --set password="$1"

helm delete --purge get-tweets-api || echo "Installing it now"
helm upgrade --install get-tweets-api ./infra/application/ -f ./get-tweets-api/env/values.yaml