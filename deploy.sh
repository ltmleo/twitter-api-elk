#!/bin/bash
set -e
 

print_help() {
            echo "Uso: $0 [OPÇÕES]..."
            echo 'Script para auxiliar no deploy'
            echo
            echo '-a    Realiza deloy de todas release'
            echo '-i    Realiza depoy das releases de ferramentas'
            echo '-u    Realiza deploy das releases das aplicações'
            echo '-p    OBRIGATORIO: passord para relizar deploy da aplicação save-tweets'
            echo '-h    Exibe ajuda.'
}

all() {
    update_infra
    update_apps
}

update_infra(){
    helm upgrade --install elastic   ./infra/elk-stack/elasticsearch/ -f ./infra/elk-stack/elasticsearch/values.yaml
    helm upgrade --install filebeat   ./infra/elk-stack/filebeat/ -f ./infra/elk-stack/filebeat/values.yaml
    helm upgrade --install apm-server   ./infra/elk-stack/apm-server/ -f ./infra/elk-stack/apm-server/values.yaml
    helm upgrade --install logstash   ./infra/elk-stack/logstash/ -f ./infra/elk-stack/logstash/values.yaml
    helm upgrade --install metricbeat   ./infra/elk-stack/metricbeat/ -f ./infra/elk-stack/metricbeat/values.yaml
    helm upgrade --install kibana   ./infra/elk-stack/kibana/ -f ./infra/elk-stack/kibana/values.yaml
    helm upgrade --install mongodb   ./infra/mongodb/ -f ./infra/mongodb/values.yaml
}

update_apps(){
    test $PASSWORD || (echo "[ERROR] missing password" && print_help && exit 1)
    helm upgrade --install  save-tweets ./infra/application/ -f ./save-tweets/env/values.yaml --set password=${PASSWORD}
    helm upgrade --install  get-tweets-api ./infra/application/ -f ./get-tweets-api/env/values.yaml
    helm upgrade --install  web-interface ./infra/application/ -f ./web-interface/env/values.yaml
}

delete(){
    helm delete --purge apm-server elastic filebeat get-tweets-api kibana \
                        logstash metricbeat mongodb save-tweets
}

while getopts 'p:ad:iuh' opt ; do
    case ${opt} in
        p)  export PASSWORD="${OPTARG}";;
        a)  all;;
        d)  delete "$OPTARG";;
        i)  update_infra;;
        u)  update_apps;;
        h)  print_help && exit 0;;
        *)  exit 1;;
    esac
done


#helm delete --purge save-tweets || echo "Installing it now"
#helm upgrade --install save-tweets ./infra/application/ -f ./save-tweets/env/values.yaml --set password="$1"

#helm delete --purge get-tweets-api || echo "Installing it now"
#helm upgrade --install get-tweets-api ./infra/application/ -f ./get-tweets-api/env/values.yaml