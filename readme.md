## Deploy

Install `awscli`

https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html

and `sam`

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html

Install Libraries

```
pip3 install -r requirements.txt -t ../
```

```
sam package --template-file template.yaml --s3-bucket nutile-sam --s3-prefix sam-build --output-template-file \
packaged.yaml
```

then

```
sam deploy --template-file ./packaged.yaml --stack-name example-staing --capabilities CAPABILITY_NAMED_IAM \
--region=us-east-1
```

## Testing

```
python3 -m unittest test_foo
```
