nkem

cat << EOF | kubectl apply -f -
apiVersion: spv.no/v1alpha1
kind: AzureKeyVaultSecret
metadata:
  name: ${KEY_VAULT_SECRET_NAME}
  namespace: akv2k8s-test
spec:
  vault:
    name: ${KEY_VAULT_NAME}             # name of key vault
    object:
      name: ${KEY_VAULT_SECRET_NAME}    # name of the akv object
      type: secret                      # akv object type
EOF

KEY_VAULT_NAME='vaultos'
KEY_VAULT_SECRET_NAME='sqlpassword' 
________________________________________________________

cat << EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: akv2k8s-test
  namespace: akv2k8s-test
spec:
  containers:
  - name: akv2k8s-env-test
    image: spvest/akv2k8s-env-test:2.0.1
    args: ["TEST_SECRET"]
    env:
    - name: TEST_SECRET
      value: "${KEY_VAULT_SECRET_NAME}@azurekeyvault" # ref to akvs
EOF
# set up multifile secrete for akv2k8s
#for loop in bash shell for base 64 encoding of list of string

for i in {nkeamkolam ibidun chinonye lizzy}; do   echo ${i};  echo ${i}|base64; done

az keyvault secret set --name sqlpassword --vault-name vaultos --file secret.yaml

cat << EOF | kubectl apply -f -
apiVersion: spv.no/v1alpha1
kind: AzureKeyVaultSecret
metadata:
  name: msecrete
  namespace: akv2k8s-test
spec:
  vault:
    name: vaultos
    object:
      name: msecrete
      type: multi-key-value-secret # akv object type
      contentType: application/x-yaml
  output:
    secret:
      name: msecret # kubernetes secret name
      dataKey: Data
EOF